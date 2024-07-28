from tkinter import *
from PIL import Image,ImageTk

win=Toplevel()
win.title("Login system")
win.geometry("1500x850")
#back image
img = Image.open("D:\\Savingbank\\patil4.jpg")
img=img.resize((1600,850))
my = ImageTk.PhotoImage(img)
label = Label(win, image=my)
label.pack(side=LEFT,fill=BOTH,expand=True)
#back image

title=Label(win,text=" WELCOME TO STATE BANK OF INDIA ",font=("algerian",35,"bold"),fg="lightblue",bg="black")
title.place(x=200,y=0)

def app_rec():
    import applicant_form
    return
def dep_rec():
    import deposit
    return
def with_rec():
    import withdraw
    return
def int_rec():
    import interest
    return
def cl_acc_rec():
    import close_acc
    return
b1=Button(win,text="Applicant Form",font=("times new roman",25),width=18,bd=2,bg="lightblue",fg="black",command=app_rec)
b1.place(x=310,y=160)

b2=Button(win,text="Deposite",font=("times new roman",25),width=18,bd=2,bg="lightblue",fg="black",command=dep_rec)
b2.place(x=420,y=260)

b3=Button(win,text="Withdraw",font=("times new roman",25),width=18,bd=2,bg="lightblue",fg="black",command=with_rec)
b3.place(x=520,y=360)

b4=Button(win,text="Interest",font=("times new roman",25),width=18,bd=2,bg="lightblue",fg="black",command=int_rec)
b4.place(x=620,y=460)

b5=Button(win,text="Close Account",font=("times new roman",25),width=18,bd=2,bg="lightblue",fg="black",command=cl_acc_rec)
b5.place(x=720,y=560)

b2=Button(win,text="Exit",font=("times new roman",25),width=18,bd=2,fg="black",bg="lightblue",command=quit)
b2.place(x=820,y=660)

win.mainloop()