return_date=int(input("enter the return_date="))
due_date=int(input("enter the due_date="))

return_month=int(input("enter the return_month="))
due_month=int(input("enter the due_month="))
return_year=int(input("enter the return_year="))
due_year=int(input("enter the due_year="))

month=int(input("enter the month from 1-12"))
if month==2:
   year=int(input("enter the year"))
   if year%4:
      if year%100:
         if year%400:
            print(29)
      else:
            print(28)
   else:
      print(29)
if month==1,3,5,




            
            



# if return_date==due_date and return_month==due_month and return_year==due_year:
#    print("no fine")
# elif return_date!=due_date and return_month==due_month and return_year==due_year:
#       print("fine",(return_date-due_date)*15)
# elif return_date==due_date and return_month!=due_month and return_year==due_year:
#    print("fine",(return_month-due_month)*500)
# elif return_date!=due_date and return_month!=due_month and return_year==due_year:
#    print("fine",(return_date-due_year)*15+(return_month-due_month)*500)
# elif return_date==due_date and return_month==due_month and return_year!=due_year:
#    print("fine",(return_year-due_year)*10000)
# elif return_date!=due_date and return_month==due_month and return_year!=due_year:
#    print("fine",(return_date-due_date)*15+(return_year-due_year)*10000)

# elif return_date!=due_date and return_month!=due_month and return_year!=due_year:
#    print("fine",(return_date-due_date)*15+(return_month-due_month)*500+(return_year-due_year)*10000)














