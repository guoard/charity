# charity

هدف از پروژه این دوره طراحی بستری اینترنتی برای ایجاد ارتباط بین مراکز خیریه و نیکوکاران است تا به این ترتیب برقراری ارتباط بین خیرین و نیازمندهای موجود تسهیل گردد. از آن‌جایی که برخی از نیازمندی‌های موجود، ماهیتی غیر نقدی دارند و نیازمند مهارت و تخصص فردی هستند، وجود سامانه‌ای که به صورت سیستماتیک این نیازمندی‌ها را مشخص و با افراد توانمند و متناسب مرتبط سازد احساس می‌شود. به عنوان مثال توانایی نگه‌داری از سالمندان یا کودکان و یا تخصص در حیطه‌ای آموزشی برای تدریس داوطلبانه در منطقه‌ای محروم دسته‌ای از نیازمند‌ی‌ها هستند که در دسته‌ی نیازمندی‌های غیر نقدی قرار می‌گیرند و نیاز به فردی متخصص دارند

مکانیزم کلی این سامانه به این صورت است که در آن مراکز خیریه نیازهای خود را در قالب پروژه تعریف کرده و نیکوکاران از بین این نیازها مورد یا مواردی که با توانمندی و زمان آن‌ها سازگار است را انتخاب می‌کنند و برای آن درخواست می‌دهند. پروژه‌های تعریف شده دارای مشخصات و نیازمندی‌هایی هستند که شخص نیکوکار می‌تواند با جست‌و‌جو بر اساس این مشخصات پروژه‌ی مطلوب خود را بیابد. سپس موسسه‌ی خیریه با در نظر گرفتن شرایط نیکوکار می‌تواند درخواست وی را رد و یا قبول کند

* کاربران(چه موسسه‌ها و چه نیکوکاران) می‌توانند در این سیستم عضویت پیدا کنند
* نیکوکاران می‌توانند درخواست بدهند برای یک نیازمندی که آن را می‌خواهند انجام دهند
* موسسه‌ها می‌توانند طبق شرایط بپذیرند که این عمل را این نیکوکار انجام دهد و یا خیر
* موسسه‌ها می‌توانند در صورت تمام شدن یک نیازمندی آن را تمام شده اعلام کنند

## Project Models

در پروژه دو نوع مدل Charity و Benefactorوجود دارد که کاربران می‌توانند یکی از این دو نوع کاربر باشند. با این که این دو نوع کاربر تفاوت‌های زیادی دارند اما به دلیل اشتراک‌هایشان از یک مدل مشترک به نام User ارث می‌برند. برای ثبت‌نام در سایت کاربر در ابتدا باید به وسیله‌ی مدل User ثبت‌نام کند و سپس بنا به نوع کاربری باید از طریق Charity و یا Benefactor ثبت‌نام‌‌شان را نهایی کنند. در این سوال وظیفه‌ی شما پیاده‌سازی ثبت‌نام برای User می‌باشد.

![image](https://uupload.ir/files/c19y_charity2.png)