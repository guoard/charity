from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsCharityOwner, IsBenefactor
from charities.models import Task
from charities.serializers import (
    TaskSerializer, CharitySerializer, BenefactorSerializer
)


class BenefactorRegistration(generics.CreateAPIView):
    serializer_class = BenefactorSerializer
    # queryset = Benefactor.objects.all()

    def post(self, request):
        benefactor_serialize = BenefactorSerializer(data=request.data)
        if benefactor_serialize.is_valid():
            benefactor_serialize.save(user=request.user)
            return Response({'message': 'benefactor created successfully!'})
        return Response({'message': benefactor_serialize.errors})

    permission_classes = (IsAuthenticated,)


class CharityRegistration(generics.CreateAPIView):
    serializer_class = CharitySerializer
    # queryset = Charity.objects.all()

    def post(self, request):
        charity_serializer = CharitySerializer(data=request.data)
        if charity_serializer.is_valid():
            charity_serializer.save(user=request.user)
            return Response({'message': 'charity created successfully!'})
            # TODO: Object of type Charity is not JSON serializable(return object not message)
        return Response({'message': charity_serializer.errors})

    permission_classes = (IsAuthenticated,)


class Tasks(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all_related_tasks_to_user(self.request.user)

    def post(self, request, *args, **kwargs):
        data = {
            **request.data,
            "charity_id": request.user.charity.id
        }
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsCharityOwner, ]

        return [permission() for permission in self.permission_classes]

    def filter_queryset(self, queryset):
        filter_lookups = {}
        for name, value in Task.filtering_lookups:
            param = self.request.GET.get(value)
            if param:
                filter_lookups[name] = param
        exclude_lookups = {}
        for name, value in Task.excluding_lookups:
            param = self.request.GET.get(value)
            if param:
                exclude_lookups[name] = param

        return queryset.filter(**filter_lookups).exclude(**exclude_lookups)


class TaskRequest(APIView):
    permission_classes = (IsBenefactor,)

    def get(self, request, task_id):
        obj = get_object_or_404(Task, pk=task_id)
        if obj.state != Task.TaskStatus.PENDING:
            return Response(data={'detail': 'This task is not pending.'}, status=404)

        Task.assign_to_benefactor(obj, request.user.benefactor)
        return Response(data={'detail': 'Request sent.'}, status=200)


class TaskResponse(APIView):
    permission_classes = (IsCharityOwner,)
    class_serializer = TaskSerializer

    def post(self, request, task_id):

        obj = get_object_or_404(Task, pk=task_id)
        response = request.data.get('response')
        if response != 'A' and response != 'R':
            return Response(data={'detail': 'Required field ("A" for accepted / "R" for rejected)'}, status=400)
        if obj.state != Task.TaskStatus.WAITING:
            return Response(data={'detail': 'This task is not waiting.'}, status=404)

        Task.response_to_benefactor_request(obj, response)
        return Response(data={'detail': 'Response sent.'}, status=200)

        # if response == 'A':
        #     obj.state = Task.TaskStatus.ASSIGNED
        #     obj.save()
        #     return Response(data={'detail': 'Response sent.'}, status=200)
        # elif response == 'R':
        #     obj.state = Task.TaskStatus.PENDING
        #     obj.assigned_benefactor = None
        #     obj.save()
        #     return Response(data={'detail': 'Response sent.'}, status=200)


class DoneTask(APIView):

    def post(self, request, task_id):
        obj = get_object_or_404(Task, pk=task_id)
        if obj.state != Task.TaskStatus.ASSIGNED:
            return Response(data={'detail': 'Task is not assigned yet.'}, status=404)
        Task.done(obj)
        return Response(data={'detail': 'Task has been done successfully.'}, status=200)
