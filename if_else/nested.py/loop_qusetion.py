# # Write a Python program to check the validity of password 
# # input by users. Go to the editor
# # Validation :
# # At least 1 letter between [a-z] and 1 letter between [A-Z].
# # At least 1 number between [0-9].
# # At least 1 character from [$#@].
# # Minimum length 6 characters.
# # Maximum length 16 characters.

# # import re
# # a=input("enter the password")
# # x=True
# # while x:
# #    if  (len(a)<6 or len(a)>12):
# #       break
# #    elif not re.search("[a-z]",a):
# #       break
# #    elif not re.search("[A-Z]",a):
# #       break
# #    elif not re.search("[1-9]",a):
# #       break
# #    elif not re.search("[@#$]",a):
# #       break
# #    elif re.search("/s",a):
# #       break
# #    else:
# #       print("valid password")
# #       x=False
# #       break
# # if x:
# #    print("invalid password")


# # Write a Python program to find numbers between 100 and 
# # 400 (both included) where each digit of a number is an 
# # even number. The numbers obtained should be printed in 
# # a comma-separated sequence. 

# # item=0
# # for i in range(100,400):
# #    s=str(i)
# #    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
# #       item=i
# #       print((item),end=",")


# # Write a Python program to calculate a dog's age in dog's years
# # 
# # human_age=int(input("enter dogs age in human year"))
# # if human_age<=2:
# #    dog_age=human_age*10.5
# # else:
# #    dog_age=(21+(human_age-2)*4)
# # print("dogs age in dogs year",dog_age)


# # Write a Python program to check whether an alphabet is
# # vowel or consonant
# # user=input("enter the letter")
# # if user in ("a","e","i","o","u"):
# #    print("vowel")
# # else:
# #    print("consonant")


# # Write a Python program to sum of two given integers. 
# # However, if the sum is between 15 to 20 it will return 20

# # x=int(input("enter the number"))
# # y=int(input("enter the second"))
# # sum=x+y
# # if sum in range(15,20):
# #    print(20)
# # else:
# #    print(sum)


# # print("month:jan,feb,march,april,may,june,july,august,september,october,november,december")

# # month=input("enter the month name:")
# # if month in ("jan","march","may","july","september","november"):
# #    print(31,"days")
# # elif month in ("april","june","august","ocyober","december"):
# #    print(30,"days")
# # elif month in("feb"):
# #    print(28,"days")
# # else:
# #    print("wrong month")


   
# # Write a Python program to check a triangle is equilateral, 
# # isosceles or scalene.

# # x=int(input("first side of triangle"))
# # y=int(input("second side of triangle"))
# # z=int(input("third side of triangle"))
# # if x==y and x==z and y==z:
# #    print("equilateral")
# # elif x!=y and x==z and y==z:
# #    print("isosceles")
# # else:
# #    print("scalene")


# # Write a Python program to display astrological sign for 
# # given date of birthWrite a Python program to display 
# # astrological sign for given date of birth

# # day=int(input("enter the day"))
# # month=input("enter the month")
# # if month=="april":
# #    if day<19:
# #       print("aries")
# #    else:
# #       print("taurus")
# # if month=="may":
# #    if day<20:
# #       print("taurus")
# #    else:
# #       print("gemini")
# # if month=="june":
# #    if day<21:
# #       print("gemini")
# #    else:
# #       print("cancer")
# # if month=="july":
# #    if day<22:
# #       print("cancer")
# #    else:
# #       print("leo")
# # if month=="august":
# #    if day<22:
# #       print("leo")
# #    else:
# #       print("virgo")
# # if month=="september":
# #    if day<22:
# #       print("virgo")
# #    else:
# #       print("libra")
# # if month=="october":
# #    if day<23:
# #       print("libra")
# #    else:
# #       print("scorpius")
# # if month=="november":
# #    if day<21:
# #       print("scorpius")
# #    else:
# #       print("sagittarius")
# # if month=="december":
# #    if day<21:
# #       print("sagittarius")
# #    else:
# #       print("capricornus")
# # if month=="january":
# #    if day<19:
# #       print("capricornus")
# #    else:
# #       print("aquarius")
# # if month=="february":
# #    if day<18:
# #       print("aquarius")
# #    else:
# #       print("pisces")
# # if month=="march":
# #    if day<20:
# #       print("pisces")
# #    else:
# #       print("aries")
   

# # Write a Python program to display the sign of the Chinese 
# # Zodiac for given year in which you were born
 
 
#year=int(input("enter the year"))
   
# if year%12==0:
#       print("monkey")
# elif year%12==1:
#       print("rooster")
# elif year%12==2:
#       print("dog")
# elif year%12==3:
#       print("pig")
# elif year%12==4:
#       print("rat")
# elif year%12==5:
#       print("ox")
# elif year%12==6:
#       print("tiger")
# elif year%12==7:
#       print("rabbit")
# elif year%12==8:
#       print("dragon")
# elif year%12==9:
#       print("snake")
# elif year%12==10:
#       print("horse")
# elif year%12==11:
#       print("sheep")
# else:
#       print("invalid year")
     

#  Write a Python program to find the median of three values
# a=int(input("enter the first number"))
# b=int(input("enter the second number"))
# c=int(input("enter the third number"))
# if b<a<c:
#       print("median",a)
# if a<b<c:
#       print("median",b)
# else:
#       print("median",c)



# # Write a Python program to create the multiplication table 
# # (from 1 to 10) of a number

# # a=int(input("enter the number"))
# # for i in range(1,11):
# #    print(a,"X",i,"=",a*i)
  
  
   
# # Write a Python program that reads two integers representing 
# # a month and day and prints the season for that month and day

# # month=input("enter the month=")
# # days=int(input("enter the day="))
# # if month in("feb","march","april"):
# #    if days<=31:
# #       print("spring")
# # if month in("may","june","july"):
# #    if days<=31:
# #       print("summer")
# # if month in("aug","sept","oct"):
# #    if days<=31:
# #       print("autumn")
# # if month in("nov","dec","jan"):
# #    if days<=31:
# #       print("winter")

# # hakacton task: calculator using itinker
# # def add(x,y):
# #    print(x+y)
# # def subtract(x,y):
# #    print(x-y)
# # def multiply(x,y):
# #    print(x*y)
# # def divide(x,y):
# #    print(x/y)
# # print("enter the operation")
# # print("1.add")
# # print("2.subtract")
# # print("3.multiply")
# # print("4.divide")
# # while True:
# #    choice=input("enter the choice(1/2/3/4):")
# #    num1=float(input("enter the first number"))
# #    num2=float(input("enter the second number"))
# #    if choice=="1":
# #        print(add(num1,num2))
# #    elif choice=="2":
# #       print(subtract(num1,num2))
# #    elif choice=="3":
# #       print(multiply(num1,num2))
# #    elif choice=="4":
# #       print(divide(num1,num2))
# #    else:
# #       print("invalid input")
# #       break



# n=int(input("enter the number:"))
# i=1
# sum=0
# average=0
# while i<=n:
#    number=int(input("enter the number:"))
#    sum=sum+number
#    i+=1
# print(sum)
# average=sum/number
# print(average)
   
   
# for row in range(7):
#    for column in range(5):
#       if (row==0 and column%4!=0) or (row==3 and column%4!=0) or (row!=0 and column==0) or (row!=0 and column==4):
#          print("*",end=" ")
#       else:
#          print(" ",end=" ")
#    print()

   

# t=0
# a=1
# average=0
# while a<=11:
#    weight=int(input("Enter the weight:"))
#    t=t+weight
#    a=a+1
#    average=t/11
# print(average)
# if average%5==0:
#    print("Divisible")
# else:
#    print("Not Divisible")


# write a python program to print alphabet A.



# for row in range (7):
#    for col in range(5):
#       if (row==0 and col%4!=0) or (row==3) or (col==0 and row!=0) or (col==4 and row!=0):
       
#          print("*",end="")
#       else:
#          print(" ",end="")
#    print()

# write a python program to print alphabet B

# for row in range(7):
#    for col in range(5):
#       if (row==0 and col%4!=0):
#          print("*",end="")
#       else:
#          print(" ",end="")
#    print()
   

   
   
###################################################

# x=1500
# while x<=2500:
#    if x%5==0 and x%7:
#          print("divisible")
#    else:
#       print(x)
#    x+=1

# x=0
# g=7
# while x<=6:
#    guess=int(input("enter the guess number"))
#    if guess!=g:
#       print("try again")
#    else:
#       print('right')
#       break
#    x+=1
 
# i=10
# while i>=1:
#    print(i)
#    i-=1

# i=0
# while i<=10:
#    print(i)
# i+=1

# x= int(input(""))
# y=int(input(""))
# z=int(input(""))
# a=int(input(""))
# if x<y and x<z and x<a:
#    print(x ,"x is the smallest")
# elif y<z and y<x and z<a:
#    print(y,"y is the smallest")
# elif z<a and z<x and z<y:
#    print(z,"z is the samllest")
# elif a<x and a<y and a<z:
#    print(a,"a is the smallest")

# user=int(input(""))
# if user%5==0:
#    if user%11==0:
#       print("divisible by 5 and 11")
#    else:
#       print('divisible by 5')
# else:
#    print("not divisible")





# year=int(input("enter the year"))
# if year%4==0:
#    if year%100==0:
#       if year%400==0:
#          print('leap year')
#       else:
#          print("not leap year")
#    else:
#       print(" leap year")
# else:
#    print(" not leap year")


# i=1
# while i<=5:
#    if i%2==0:
#       print('*',end="")
#    i+=1
# else:
#    print(i,end="")
      

# for i in range(7):
#    for j in range(1,i):
#       print(j,end=" ")
#    print()
   
   
# for i in range(7):
#    for j in range(1,i):
#       if j%2==0:
#          print("*",end=" ")
#       else:
#          print(j,end=" ")
#    print()

# for i in range(7):
#    for j in range(1,i):
#       if i%2!=0:
#          print("*",end="")
#       else:
#           print(j,end="")
#    print()
      
# a=int(input("enter the number of terms"))
# b=0
# c=1
# if a<=0:
#    print(b)
# else:
#    print(b,c,end=" ")
#    for x in range(a):
#       next=b+c
#       print(next,end=" ")
#       b=c
#       c=next

# x=int(input("enter the first number"))
# y=int(input("enter the second condition"))
# i=1
# hcf=0
# while i<=x and i<=y:
#    if x%i==0 and y%i==0:
#       hcf=i
      
#    i=i+1
# print(hcf)


# l=0
# d=0
# user=input("enter the string")
# for x in (user):
#    if user.isdigit():
#      d=d+1
#    elif user.isalpha():
#      l=l+1
#    else:
#      pass
# print('number of digit:',d)
# print('number of alph:',l)

# l=0
# d=0
# x=input("enter the string")
# for i in (x):
#    if i.isdigit():
#       d=d+1
#    elif i.isalpha():
#       l=l+1
#    else:
#       pass
# print(l)
# print(d)
# import re
# ps=input("enter the password")
# x=True
# while x:
#    if (len(ps)<6 or len(ps)>12):
#       break
#    elif not re.search ("[a-z]",ps):
#       break
#    elif not re.search ("[A-Z]",ps):
#       break
#    elif not re.search ("[1-9]",ps):
#       break
#    elif not re.search ("[@#$]",ps):
#       break
#    elif re.search("/s",ps):
#       break
#    else:
#       print("valid")
#       x=False
#       break
# while x:
#    print("invallid password")
      
# for  i in range(6):
#    for j in range(1,6):
#       print(i,end=" ")
#    print()



