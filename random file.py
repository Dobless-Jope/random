from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import os
import csv

screen=Tk()
screen.geometry('600x300')
screen.title("Details")
def registration():
    u1=reg_username.get()
    u2=reg_password.get()
    u3=reg_age.get()
    u4=reg_gender.get()
    a=os.listdir()
    if u1 == "" or u2 =="" or u3=="" or u4 == "":
        reg_notif.config(text="All fields are necessary",fg="red")
        return
    for i in a:
        if u1 == i:
            reg_notif.config(fg="red",text="Account already exists")
            return
        else:
            file=open(u1,"w")
            file.write(u1+'\n')
            file.write(u2+'\n')
            file.write(u3+'\n')
            file.write(u4)
            file.close()
            reg_notif.config(fg="green",text="Account has been created")
            screen1.after(1000,lambda:screen1.destroy())

def register():
    global screen1
    global reg_username
    global reg_password
    global reg_age
    global reg_gender
    global username_reg
    global password_reg
    global age_reg
    global reg_notif
    screen1=Toplevel(screen)
    screen1.title("Registration page")
    screen1.geometry('600x300')
    reg_username=StringVar()
    reg_password=StringVar()
    reg_age=StringVar()
    reg_gender=StringVar()
    Label(screen1,text="Please enter details necessary for registration below").pack()
    Label(screen1,text="Characters are not case sensitive").pack()
    Label(screen1,text="Note: No changes can be made later on to your registration details").pack()
    Label(text="").pack()
    Label(screen1,text="Username").pack()
    username_reg=Entry(screen1,textvariable=reg_username)
    username_reg.pack()
    Label(screen1,text="Password").pack()
    password_reg=Entry(screen1,textvariable=reg_password,show='*')
    password_reg.pack()
    Label(screen1,text="Age").pack()
    age_reg=Entry(screen1,textvariable=reg_age)
    age_reg.pack()
    Label(screen1,text="Gender").pack()
    gender_reg=Entry(screen1,textvariable=reg_gender)
    gender_reg.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Register",width="10",height="1",command=registration).pack()
    reg_notif=Label(screen1)
    reg_notif.pack()

def maindatabase():
    screen5=Toplevel(screen)
    screen5.title('Event database')
    screen5.geometry("1540x800+0+0")
    Label(screen5,bd=20,relief=RIDGE,text="EVENT MANAGEMENT DATABASE",bg="white",font=("times new roman",50,"bold")).pack(side=TOP,fill=X)
    f1=Frame(screen5,bd=20,relief=RIDGE)
    f1.place(x=0,y=130,width=1530,height=400)
    lf1=LabelFrame(f1,bd=10,relief=RIDGE,padx=10,
                                              font=("times new roman",12,"bold"),text="Information about the event")
    lf1.place(x=0,y=5,width=980,height=350)
    lf2=LabelFrame(f1,bd=10,relief=RIDGE,padx=10,
                                              font=("times new roman",12,"bold"),text="Details overview")
    lf2.place(x=990,y=5,width=460,height=350)
    ff1=Frame(screen5,bd=20,relief=RIDGE)
    ff1.place(x=0,y=530,width=1530,height=70)
    df1=Frame(screen5,bd=20,relief=RIDGE)
    df1.place(x=0,y=600,width=1530,height=190)
    l1=Label(lf1,text='Name of the user',font=("times new roman",12,"bold"),padx=2,pady=6)
    l1.grid(row=0,colum=0)


def d1():
    screen4.destroy()
def userinfo():
    u1=log_username.get()
    a=os.listdir()
    for i in a:
        if u1 == i:
            file=open(i,'r')
            k=file.read()
            m=u1
            global screen4
            screen4=Toplevel(screen)
            screen4.title("User info ")
            screen4.geometry("400x170")
            Label(screen4,text="Your username is"+":"+" "+m).pack()
            Label(screen4,text="").pack()
            Button(screen4,text="Return to account dashboard",command=d1).pack()
            file.close()
def gologin():
    u1=log_username.get()
    u2=log_password.get()
    a=os.listdir()
    for i in a:
        if i == u1:
            file=open(i,"r")
            file_data=file.read()
            file_data=file_data.split('\n')
            j=file_data[1]
            if u2 == j:
                screen2.destroy()
                screen3=Toplevel(screen)
                screen3.title('Account Dashoard')
                screen3.geometry('600x300')
                Label(screen3,text="Welcome to your account dashboard"+" "+u1).pack()
                Label(screen3,text="").pack()
                Label(screen3,text="Here is a list of things you might want to check out").pack()
                Label(screen3,text="").pack()
                Button(screen3,text="User details",width="15",height="1",command=userinfo).pack() 
                Label(screen3,text="").pack()
                Button(screen3,text="Event database",width="15",height="1",command=maindatabase).pack() 
                Label(screen3,text="").pack()
                Button(screen3,text="Contact an event manager",height="1").pack() 
                return
            else:
                login_notif.config(text="Password entered in incorrect",fg='red')
                return
        
        login_notif.config(text="No such account exists in the database",fg="red")

def login():
    global screen2
    global log_username
    global log_password
    global username_log
    global password_log
    global login_notif
    screen2=Toplevel(screen)
    screen2.geometry('300x180')
    log_username=StringVar()
    log_password=StringVar()
    Label(screen2,text="Please enter details").pack()
    Label(text="").pack()
    Label(screen2,text="Username").pack()
    username_log=Entry(screen2,textvariable=log_username)
    username_log.pack()
    Label(screen2,text="Password").pack()
    password_log=Entry(screen2,textvariable=log_password,show='*')
    password_log.pack()
    Label(screen2,text="").pack()
    Button(screen2,text="Login",width="10",height="1",command=gologin).pack()
    login_notif=Label(screen2)    
    login_notif.pack()



Label(text="Please click on one of the below options to continue",font='16',width='300',height='2').pack()
Label(text="").pack()
Button(text="Login",height="3",width="30",command=login).pack()
Label(text="").pack()
Button(text="Register",height="3",width="30",command=register).pack()
screen.mainloop()
