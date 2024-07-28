from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import random
from tkinter import messagebox

import pyttsx3
converter = pyttsx3.init()
converter.setProperty('rate', 150)
converter.setProperty('volume', 0.7)
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
converter.setProperty('voice', voice_id)
def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management system")
        self.root.geometry("1550x800+0+0")

        #===============Background Images========================
        img = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\hotel01.jpg")
        img = img.resize((1550, 800), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        lblimg = Label(self.root, image=self.photoimg, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=800)

        #============frme==========
        frame = Frame(self.root,bg='black')
        frame.place(x=610, y=170, width=340, height=450)

        #======================logo======================
        img1 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\patil6.jpg")
        img1 = img1.resize((100, 100), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1,  bg='black',borderwidth=0)
        lblimg.place(x=730, y=175, width=100, height=100)

        #lable
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), bg='black',fg="white")
        get_str.place(x=95,y=100)

        username=lbl=Label(frame,text='Username',font=("times new roman", 15, "bold"), bg='black',fg="white")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text='Password',font=("times new roman", 15, "bold"), bg='black',fg="white")
        password.place(x=70,y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"),show='*')
        self.txtpass.place(x=40, y=250, width=270)

        #==============Icon Images=====
        img2 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\patil6.jpg")
        img2 = img2.resize((25, 25), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bg='black', borderwidth=0)
        lblimg.place(x=650, y=323, width=25, height=25)

        img3 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\lock4.jpg")
        img3 = img3.resize((25, 25), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bg='black', borderwidth=0)
        lblimg.place(x=650, y=395, width=25, height=25)

        #login button
        loginbtn = Button(frame, text="Login", command=self.login, width=22,font=("times new roman", 15, "bold"), bg='red',activeforeground='white',activebackground='red', fg="white",relief=RIDGE, bd=3, cursor="heart")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        registerbtn = Button(frame, text="New User Register", command=self.rigister_window,width=22, font=("times new roman", 10, "bold"), bg='black',
                          activeforeground='white', activebackground='black', fg="white", border=0,
                          cursor="heart")
        registerbtn.place(x=15, y=350, width=160)

        #forget pass btn
        forgenbtn = Button(frame, text="Forget Password", command=self.forgot_password_window,width=22, font=("times new roman", 10, "bold"), bg='black',
                          activeforeground='white', activebackground='black', fg="white",border=0,
                          cursor="heart")
        forgenbtn.place(x=10, y=370, width=160)

    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            converter.say("all field required")
            converter.runAndWait()
            messagebox.showerror("Error","all field required")

        else:
            conn = mysql.connector.connect(
                username="root",
                password="",
                host="localhost",
                database="hotel"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","open the project")
                if open_main>0:
                    converter.say("Great Welcom to my Hotel Management System Project")
                    converter.runAndWait()
                    self.new_window=Toplevel(self.root)
                    import bank_acc_sys
                    return

                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
#=====================reset password=========================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select sucurity Quetion",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(
                username="root",
                password="",
                host="localhost",
                database="hotel"
            )
            my_cursor = conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Plaese enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, plaese login new password",parent=self.root2)


#==========================forgot_password_window====================================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please Enter the Email address to reset password",parent=self.root)
        else:
            conn = mysql.connector.connect(
                username="root",
                password="",
                host="localhost",
                database="hotel"
            )
            my_cursor = conn.cursor()
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,'bold','underline'),fg='red',bg='white',width=21,relief=RIDGE)
                l.place(x=0,y=20,width=339,height=40)

                security_Q = Label(self.root2, text="Select Security Quetions:", font=("times new roman", 15, "bold"),
                                   bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("arial", 13, "bold"),
                                                     width=27,
                                                     state="readonly")
                self.combo_security_Q["value"] = ("Select", "Your Birth Place", "Your BestFriend Name", "Your Pet Name")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50, y=110, width=250)

                security_A = Label(self.root2, text="Security Answer:",
                                   font=("times new roman", 15, "bold"), bg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password:",
                                   font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15, "bold"),fg='white',bg='dark green')
                btn.place(x=100,y=290)
                #sabir@gmail.com

#==========================ANOTHER CLASS====================================
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management system")
        self.root.geometry("1550x800+0+0")
        #+===============variables=========
        self.var_fname=StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ= StringVar()
        self.var_securityA = StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()


        #==============bg Image==================
        img = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\wallpape.jpg")
        img = img.resize((1550, 800), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        lblimg = Label(self.root, image=self.photoimg, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=800)

        #================left image=================
        img1 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\very.jpg")
        img1 = img1.resize((470, 550), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=50, y=100, width=470, height=550)

        # ============frme==========
        frame = Frame(self.root, bg='white')
        frame.place(x=520, y=100, width=800, height=550)
        #lablal
        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold",'underline'), bg='white',
                          fg="dark green", bd=4)
        register_lbl.place(x=20, y=20)

        # =====================labels and entrys=================
        # -----------row1
        fname = Label(frame, text="First Name:", font=("times new roman", 15, "bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15, "bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name = Label(frame, text="Last Name:", font=("times new roman", 15, "bold"), bg="white")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname,font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        # -----------row2
        contact = Label(frame, text="Contact No:", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact= ttk.Entry(frame, textvariable=self.var_contact,font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email:", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # -----------row3
        security_Q = Label(frame, text="Select Security Quetions:", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ,font=("arial", 13, "bold"), width=27,
                                    state="readonly")
        self.combo_security_Q["value"] = ("Select","Your Birth Place","Your BestFriend Name","Your Pet Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=270,width=250)

        security_A = Label(frame, text="Security Answer:", textvariable=self.var_securityA,font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        # -----------row4
        pswd = Label(frame, text="Password:", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass,font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password:", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass,font=("times new roman", 15, "bold"))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        #=============checkbutton====================

        checkbtn=Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.var_check,font=("times new roman", 12, "bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #==============button============================
        img3 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\regester.jpg")
        img3 = img3.resize((200, 50), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(frame, image=self.photoimg3,command=self.register_data, borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=10, y=420, width=200)

        img4 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\now3.jpg")
        img4 = img4.resize((200, 45), Image.ADAPTIVE)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b2 = Button(frame, image=self.photoimg4, command=self.return_login,borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b2.place(x=330, y=420, width=200)

        #==================Fuction Delartion==============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email=="" or self.var_securityQ=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Plaese agree our terms one condition",parent=self.root)
        else:
            conn = mysql.connector.connect(
                username="root",
                password="",
                host="localhost",
                database="hotel"
            )
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get(),

                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully",parent=self.root)
    def return_login(self):
        self.root.destroy()
#==================================hotel class=============================

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management system")
        self.root.geometry("1550x800+0+0")
        #===================ist img====================
        img1=Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\hotel3.jpg")
        img1=img1.resize((1550,140),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        #===================logo=======================
        img2 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\grand.jpg")
        img2 = img2.resize((230, 140), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)
        #================Title=======================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg='black',fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        #===============in frame====================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        #============menu=======================
        lbl_title = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg='black',fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=230)
        # ===============button frame====================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=150)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman", 14, "bold"), bg='black',fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.roombooking,width=22, font=("times new roman", 14, "bold"), bg='black',fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0,pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22,command=self.details_room, font=("times new roman", 14, "bold"), bg='black',fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0,pady=1)

        #report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg='black',fg="gold", bd=0, cursor="hand1")
        #report_btn.grid(row=3, column=0,pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", command=self.logout,width=22, font=("times new roman", 14, "bold"), bg='black',fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0,pady=1)

        #=========================RIGHT IMG============================
        img3 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\hotel.jpg")
        img3 = img3.resize((1310, 595), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=595)

        #=======================down images===========================
        img4 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\taj.jpg")
        img4 = img4.resize((230, 240), Image.ADAPTIVE)
        self.photoimg4= ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=186, width=230, height=240)

        img5 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\khana.jpg")
        img5 = img5.resize((230, 190), Image.ADAPTIVE)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=190)







    def logout(self):
        import pyttsx3
        converter = pyttsx3.init()
        converter.setProperty('rate', 150)
        converter.setProperty('volume', 0.7)
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        converter.setProperty('voice', voice_id)
        converter.say("Logout your project good byeee")
        converter.runAndWait()
        self.root.destroy()



if __name__ == "__main__":
    main()