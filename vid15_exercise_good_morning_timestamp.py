import time
import calendar
from datetime import date

timestamp1= time.strftime('%H:%M:%S')

print("hello time is ",timestamp1)
timestamp=int(time.strftime('%H'))
name=input("your name please")
if(4<=timestamp<12):
    print("hey",name,"very good morning")
elif(12<=timestamp<=17):
    print("hey",name,"good afternoon")
elif(17<timestamp<=19):
    print("hey",name,"good evening")
else:
    print("hey",name,"good night")



#print whole calender
datetime=calendar.prmonth(2023,3)



#print today date
d1=time.strftime('%d/%m/%Y')
print(d1)
d2=time.strftime('%d-%B %y')
print(d2)
d3=time.strftime('%d-%b %Y')
print(d3)


