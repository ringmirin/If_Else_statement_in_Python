# print("welcome to State Bank of India")
# balance=2000
# pin_code=1234
# language=input("please select langauge:","english or hindi")
# if language=="english":
#    print("please enter your pin")
# pin=int(input("please enter the pin"))
# if pin==pin_code:
#           print("1=withdraw")
#           print("2=balance enquiry")
#           print("3=cash diposit")
          
#           c=int(input("please choose transaction"))
#           if c==1:
#                     withdraw=int(input("enter withdraw amount"))
#                     if withdraw<balance:
#                               print("please take your money:",withdraw)
#                               print("remaining balance:",balance-withdraw)
               
#                     else:
#                               print("insufficient balance")

#           elif c==2:
#                       print("your current balance is:",balance)
          
#           elif c==3:
#                       diposit=int(input("enter the amount to diposit"))
#                       print("total balance:",balance+diposit)
# if language=="hindi":
#    print("not available")
# else:
#    print("wrong pin")
#    print("please try again") 





#           # elif c==3:
#           #           new_pin=int(input("enter the new pin you want"))
#           # if pin_code==4567:
#           #           print(new_pin)
#           # elif c==4:
#           # diposit=int(input("enter the diposit amount"))
#           # if pin_code==4567:
#           #           print("total amount:",balance+diposit)






print("........welcome...........")
print("STATE BANK OF INDIA")
balance=20000
pin=1234
language=input("choose language: ,english or hindi")
if language=="english":
     pin_code=int(input("enter the pin_code"))
     if pin_code==pin:
          print("1=withdrawal")
          print("2=balance enquiry")
          print("3=cash diposit")
          c=int(input("choose the transaction"))
          if c==1:
               withdraw=int(input("enter the amount to withdraw"))
               if balance>withdraw:
                 print("enter the amount to withdraw")
                 print("remaining balance:",balance-withdraw)
                 print("thank you")
               if balance<withdraw:
                 print("insufficient balance")
          if c==2:
           print("current balance:",balance)
          if c==3:
               cash_diposit=int(input("enter the diposit amount"))
               print("total balance:",balance+cash_diposit)
     else:
          print("wrong pin")
if language=="hindi":
     print("sorry... invalid")
print("thank you for banking with us")
          



