# x=int(input("enter the first_number"))
# y=int(input("enter the second_number"))
# z=int(input("enter the third_number"))
# if x<y<z:
#    print("y is median")
# if y<x<z:
#    print("x is median")
# if x<z<x:
#    print("z is median")


year=int(input("enter the year:"))
if (year%400==0):
   leap_year="true"
elif (year%100==0):
   leap_year="false"
elif (year%4==0):
   leap_year="false"
month=int(input("enter the month[1-12]:"))
if month==(1,3,5,7,9,11):
   month_length="31"  
elif month==2:
   if leap_year:
      month_length="29"
   else:
      month_lenth="28"
else:
   month_lenth="30"
day=int(input("enter the day[1-31]:"))
if day<month_length:
   day+=1
else:
   day=1
   if month==12:
      month=1
      year+=1
   else:
      month+=1
print("the next date is[yyyy-mm-dd]"(year,month,day))






      


   

