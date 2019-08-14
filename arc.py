from tkinter import *
import random
import time

root=Tk()

text=StringVar()

l=Label(root,textvariable=text,fg="black",bg="white",font=('arial',35)).place(relx=0.3,rely=0.2)
Label(root,text="ARCTools Version 2.1.2",bg="white").place(relx=0.35,rely=0.9)
root.configure(background="white")
root.geometry("200x200")
def function():
    text.set("")
    num=str(random.randint(1,999))
    if(len(num)==1):
        num="00"+num
    elif(len(num)==2):
        num="0"+num
    else:
        num=num
    print(num)
    for i in num[::-1]:
        text.set(text.get()+i)
        root.update()
        time.sleep(0.3)

function()
Button(root,text="Run Again",command=function,bg="white").place(relx=0.34,rely=0.5)


root.mainloop()
