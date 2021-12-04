from re import match
from tkinter import*
from typing import Match
root=Tk()
root.title("simple calculator")
e=Entry(root,width=40,borderwidth=6)
e.grid(row=0,column=0,columnspan=2,padx=5,pady=5)
   
def button_add(number):
  first_number=e.get()
  global f_number
  global math
  math="addition"
  f_num=int(first_number) 
  e.delete(0,END)
def button_equal():
  second_number=e.get()
  e.delete(0,END)    
  if math=="addition":
    e.insert(0,f_num+int(second_number))
def button_clear():
    e.delete(0,END)
def button_click (number):
  current=e.get()
  e.delete(0,END)
  e.insert(0,str(current)+str(number))
   


button_1=Button(root,text="1",padx=60,pady=20,command=lambda: button_click(1))
button_2=Button(root,text="2",padx=60,pady=20,command=lambda: button_click(2))
button_3=Button(root,text="3",padx=60,pady=20,command=lambda: button_click(3))
button_4=Button(root,text="4",padx=60,pady=20,command=lambda: button_click(4))
button_5=Button(root,text="5",padx=60,pady=20,command=lambda: button_click(5))
button_6=Button(root,text="6",padx=60,pady=20,command=lambda: button_click(6))
button_7=Button(root,text="7",padx=60,pady=20,command=lambda: button_click(7))
button_8=Button(root,text="8",padx=60,pady=20,command=lambda: button_click(8))
button_9=Button(root,text="9",padx=60,pady=20,command=lambda: button_click(9))
button_0=Button(root,text="0",padx=60,pady=20,command=lambda: button_click(0))
button_add=Button(root,text="+",padx=80,pady=20,command=lambda: button_add)
button_clear=Button(root,text="clear",padx=60,pady=20,command=button_clear)
button_equal=Button(root,text="=",padx=60,pady=20,command=button_equal)
button_multiply=Button(root,text="*",padx=60,pady=20,command=button_multiply)
button_subtract=Button(root,text="-",padx=60,pady=20,command=button_subtract)
button_divide=Button(root,text="/",padx=60,pady=20,command= button_divide)

button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_6.grid(row=2,column=1)
button_7.grid(row=2,column=2)

button_8.grid(row=3,column=0)
button_9.grid(row=3,column=1)
button_0.grid(row=3,column=2)

button_add.grid(row=5,column=0)
button_clear.grid(row=5,column=1)
button_equal.grid(row=4,column=2)

button_multiply.grid(row=4,column=0)
button_subtract.grid(row=4,column=1)
button_divide.grid(row=5,column=2)








root.mainloop()










# from tkinter import*
# def btnclick(number):
#     global val
#     val=val+str(number)
#     data.set(val)


# def btnClear():
#     global val
#     val=""
#     data.set("")



# def btnEqual():
#     global val
#     result=str(eval(val))
#     data.set(result)



# root=Tk()
# root.title("my calcualtor")
# # root.geometry("362x381+500+200")
# val=""
# data=StringVar()

# dispaly=Entry(root,textvariable=data,bd=29,justify="right",bg="blue",font=("ariel",20))
# dispaly.grid(row=0,columnspan=4)
# btn7=Button(root,text="7",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(7))
# btn7.grid(row=1,column=0)
# btn8=Button(root,text="8",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(8))
# btn8.grid(row=1,column=1)
# btn9=Button(root,text="9",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(9))
# btn9.grid(row=1,column=2)
# btn4=Button(root,text="4",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(4))
# btn4.grid(row=2,column=0)
# btn5=Button(root,text="5",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(5))
# btn5.grid(row=2,column=1)
# btn6=Button(root,text="6",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(6))
# btn6.grid(row=2,column=2)
# btn1=Button(root,text="1",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(1))
# btn1.grid(row=3,column=0)
# btn2=Button(root,text="2",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(2))
# btn2.grid(row=3,column=1)
# btn3=Button(root,text="3",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(3))
# btn3.grid(row=3,column=2)
# btn0=Button(root,text="0",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(0))
# btn0.grid(row=4,column=0)
# btn_division=Button(root,text="//",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick("//"))
# btn_division.grid(row=4,column=1)
# btn_Equal=Button(root,text="=",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=btnEqual)
# btn_Equal.grid(row=4,column=2)
# btn_add=Button(root,text="+",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick("+"))
# btn_add.grid(row=1,column=3)
# btn_sub=Button(root,text="-",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick("-"))
# btn_sub.grid(row=2,column=3)
# btn_multi=Button(root,text="",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick("*"))
# btn_multi.grid(row=3,column=3)
# btn_Clear=Button(root,text="clear",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=btnClear)
# btn_Clear.grid(row=4,column=3)

# root.mainloop()