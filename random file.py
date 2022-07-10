from tkinter import *
import csv
screen=Tk()
screen.geometry('600x300')
screen.title("Details")
Label(text="Please click on one of the below options to continue",font='16',width='300',height='2').pack()

def registration():
    u1=reg_username.get()
    u2=reg_password.get()
    with open ("registration.csv",'r+',newline="") as fh:
        reader=csv.reader(fh)
        writer=csv.writer(fh)
        for i in reader:
            if u1=="" or u2=="":
                Label(screen1,text="Please enter values",fg="red").pack()
            elif u1 == i[0]:
                Label(screen1,text="Username is already present",fg="green").pack()
            elif u1 not in i:
                writer.writerow([u1,u2])
                username_reg.delete(0,END)
                password_reg.delete(0,END)
                Label(screen1,text="Registration was successful",fg="green").pack()
                screen1.after(1000,lambda:screen1.destroy())
    

def register():
    global screen1
    global reg_username
    global reg_password
    global username_reg
    global password_reg
    screen1=Toplevel(screen)
    screen.title("Registration Page")
    screen.geometry('600x300')
    reg_username=StringVar()
    reg_password=StringVar()
    Label(screen1,text="Please enter details necessary for registration below").pack()
    Label(text="").pack()
    Label(screen1,text="Username").pack()
    username_reg=Entry(screen1,textvariable=reg_username)
    username_reg.pack()
    Label(screen1,text="Password").pack()
    password_reg=Entry(screen1,textvariable=reg_password,show='*')
    password_reg.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Register",width="10",height="1",command=registration).pack()

Label(text="").pack()
Label(text="").pack()
Button(text="Login",height="3",width="30").pack()
Label(text="").pack()
Button(text="Register",height="3",width="30",command=register).pack()
screen.mainloop()

