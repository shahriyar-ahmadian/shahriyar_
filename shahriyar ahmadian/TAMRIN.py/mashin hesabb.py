import math

a = math.pi/6

print ("The value of sine of pi/6 is : ", end="")

print (math.sin(a))

print ("The value of cosine of pi/6 is : ", end="")

print (math.cos(a))

print ("The value of tangent of pi/6 is : ", end="")

print (math.tan(a))

خروجی کد بالا به ترتیب سینوس، کسینوس و تانژانت 30 درجه می‌باشد:

The value of sine of pi/6 is : 0.49999999999999994

The value of cosine of pi/6 is : 0.8660254037844387

The value of tangent of pi/6 is : 0.5773502691896257

برای تبدیل رادیان به درجه و برعکس از روش زیر می‌توان استفاده کرد:

import math

a = math.pi/6

b = 30

print ("The converted value from radians to degrees is : ", end="")

print (math.degrees(a))

print ("The converted value from degrees to radians is : ", end="")

print (math.radians(b))

متغیرهای a و b به ترتیب به رادیان و درجه هستند. این دو را به توابع radians و degree دادیم تا بتوانیم تبدیلات را انجام دهیم. خروجی کد بالا به صورا زیر می‌باشد:

The converted value from radians to degrees is : 29.999999999999996

The converted value from degrees to radians is : 0.5235987755982988
