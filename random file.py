from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import csv

screen = Tk()
screen.geometry('600x300')
screen.title("Details")


def registration():
    u1 = reg_username.get()
    u2 = reg_password.get()
    u3 = reg_age.get()
    u4 = reg_gender.get()
    a = os.listdir()
    if u1 == "" or u2 == "" or u3 == "" or u4 == "":
        reg_notif.config(text="All fields are necessary", fg="red")
        return
    for i in a:
        if u1 == i:
            reg_notif.config(fg="red", text="Account already exists")
            return
        else:
            file = open(u1, "w")
            file.write(u1+'\n')
            file.write(u2+'\n')
            file.write(u3+'\n')
            file.write(u4)
            file.close()
            reg_notif.config(fg="green", text="Account has been created")
            screen1.after(1000, lambda: screen1.destroy())


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
    screen1 = Toplevel(screen)
    screen1.title("Registration page")
    screen1.geometry('600x300')
    reg_username = StringVar()
    reg_password = StringVar()
    reg_age = StringVar()
    reg_gender = StringVar()
    Label(screen1, text="Please enter details necessary for registration below").pack()
    Label(screen1, text="Characters are not case sensitive").pack()
    Label(screen1, text="Note: No changes can be made later on to your registration details").pack()
    Label(text="").pack()
    Label(screen1, text="Username").pack()
    username_reg = Entry(screen1, textvariable=reg_username)
    username_reg.pack()
    Label(screen1, text="Password").pack()
    password_reg = Entry(screen1, textvariable=reg_password, show='*')
    password_reg.pack()
    Label(screen1, text="Age").pack()
    age_reg = Entry(screen1, textvariable=reg_age)
    age_reg.pack()
    Label(screen1, text="Gender").pack()
    gender_reg = Entry(screen1, textvariable=reg_gender)
    gender_reg.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width="10",
           height="1", command=registration).pack()
    reg_notif = Label(screen1)
    reg_notif.pack()


def exit():
    screen5.destroy()


def reset():
    name.set("")
    lf2_entry.current(0)
    budget.set("")
    lf4_entry.current(0)
    date.set("")
    location.set("")
    rt1.delete("1.0", END)


def enter():
    n = name.get()
    e = event.get()
    b = budget.get()
    m = manager.get()
    l = location.get()
    if e == 'Birthday':
        with open('Birthday.csv', 'a+', newline="") as fh:
            writer = csv.writer(fh)
            a = [n, e, b, m, l]
            writer.writerow(a)
    elif e == "Marriage":
        with open('Marriage.csv', 'a+', newline="") as m:
            writer = csv.writer(m)
            b = [n, e, b, m, l]
            writer.writerow(b)
    elif e == "Corporate Meeting":
        with open('Corporate Meeting', 'a+', newline="") as m:
            writer = csv.writer(m)
            c = [n, e, b, m, l]
            writer.writerow(c)
    elif e == "Informal Get Together":
        with open('Informal Get Together', 'a+', newline="") as m:
            writer = csv.writer(m)
            d = [n, e, b, m, l]
            writer.writerow(d)
    elif e == "Conference":
        with open('Conference', 'a+', newline="") as m:
            writer = csv.writer(m)
            f = [n, e, b, m, l]
            writer.writerow(f)
    elif e == "Seminar":
        with open('Seminar.csv', 'a+', newline="") as m:
            writer = csv.writer(m)
            g = [n, e, b, m, l]
            writer.writerow(g)
    elif e == "Award shows and competition":
        with open('Award shows and competition', 'a+', newline="") as m:
            writer = csv.writer(m)
            h = [n, e, b, m, l]
            writer.writerow(h)
    elif e == "Charity event":
        with open('Charity.csv', 'a+', newline="") as m:
            writer = csv.writer(m)
            i = [n, e, b, m, l]
            writer.writerow(i)


def overview():
    rt1.insert(END, "Name of the person:\t\t" + name.get()+"\n")
    rt1.insert(END, "Type of event:\t\t" + event.get() + "\n")
    rt1.insert(END, "Event budget:\t\t" + budget.get()+"\n")
    rt1.insert(END, "Event Manager:\t\t" + manager.get()+"\n")
    rt1.insert(END, "Date of the event:\t\t" + date.get()+"\n")
    rt1.insert(END, "Event location:\t\t" + location.get())


def maindatabase():
    global screen5
    global name
    global event
    global budget
    global date
    global location
    global manager
    global lf2_entry
    global lf4_entry
    global rt1
    screen5 = Toplevel(screen)
    screen5.title('Event database')
    screen5.geometry("900x540+0+0")
    Label(screen5, bd=20, relief=RIDGE, text="EVENT DATABASE", font=(
        "times new roman", 50, "bold")).pack(side=TOP, fill=X)

    f1 = Frame(screen5, bd=20, relief=RIDGE)
    f1.place(x=0, y=130, width=900, height=300)

    lf = LabelFrame(f1, bd=10, relief=RIDGE, text='Event details',
                    padx=10, font=("times new roman", 12, "bold"))
    lf.place(x=0, y=5, width=500, height=250)

    name = StringVar()
    event = StringVar()
    budget = StringVar()
    manager = StringVar()
    date = StringVar()
    location = StringVar()
    rt1 = StringVar()

    lf1 = Label(lf, text='Full name of the user', font=(
        "times new roman", 12, "bold"), padx=2, pady=6)
    lf1.grid(row=0, column=0)

    lf1_entry = Entry(lf, font=("times new roman", 12, "bold"),
                      textvariable=name, width=35)
    lf1_entry.grid(row=0, column=1)

    lf2 = Label(lf, text='Event to be planned', font=(
        "times new roman", 12, "bold"), padx=2, pady=6)
    lf2.grid(row=1, column=0)

    lf2_entry = ttk.Combobox(
        lf, font=("times new roman", 12, "bold"), state='readonly', width=33, textvariable=event)
    lf2_entry["values"] = ("", "Birthday", 'Marriage', 'Corporate Meeting', 'Informal Get together',
                           'Conference', 'Seminar', 'Award shows and competition', 'Charity event',)
    lf2_entry.current(0)
    lf2_entry.grid(row=1, column=1)

    lf3 = Label(lf, text='Budget for the event', font=(
        "times new roman", 12, "bold"), padx=2, pady=6)
    lf3.grid(row=2, column=0)

    lf3_entry = Entry(lf, font=("times new roman", 12, "bold"),
                      width=35, textvariable=budget)
    lf3_entry.grid(row=2, column=1)

    lf4 = Label(lf, text='Event manager', font=(
        "times new roman", 12, "bold"), padx=2, pady=6)
    lf4.grid(row=3, column=0)

    lf4_entry = ttk.Combobox(
        lf, font=("times new roman", 12, "bold"), width=33, state='readonly', textvariable=manager)
    lf4_entry["values"] = ("", "Spartacus Edmundo",
                           "Maram Balder", "Husam Mirosław")
    lf4_entry.current(0)
    lf4_entry.grid(row=3, column=1)

    lf5 = Label(lf, text='Date of the event', font=(
        "times new roman", 12, "bold"), padx=2, pady=6)
    lf5.grid(row=4, column=0)

    lf5_entry = Entry(lf, font=("times new roman", 12, "bold"),
                      width=35, textvariable=date)
    lf5_entry.grid(row=4, column=1)

    lf6 = Label(lf, text='Location of the event', font=(
        "times new roman", 12, "bold"), padx=2, pady=6)
    lf6.grid(row=5, column=0)

    lf6_entry = Entry(lf, font=("times new roman", 12, "bold"),
                      textvariable=location, width=35)
    lf6_entry.grid(row=5, column=1)

    rf = LabelFrame(f1, bd=10, relief=RIDGE, text='Details overview',
                    padx=10, font=("times new roman", 12, "bold"))
    rf.place(x=510, y=5, width=350, height=250)

    rt1 = Text(rf, font=("times new roman", 12, "bold"),
               width=38, height=10, padx=2, pady=6)
    rt1.grid(row=0, column=0)

    f2 = Frame(screen5, bd=20, relief=RIDGE)
    f2.place(x=0, y=435, width=900, height=100)

    f2_button1 = Button(f2, text="Enter the data", font=(
        "times new roman", 12, "bold"), command=enter, width=22, height=2, padx=2, pady=6)
    f2_button1.grid(row=0, column=0)

    f2_button2 = f2_button1 = Button(f2, text="Delete data", font=(
        "times new roman", 12, "bold"), command=reset, width=22, height=2, padx=2, pady=6)
    f2_button2.grid(row=0, column=1)

    f2_button3 = f2_button1 = Button(f2, text="Data overview", font=(
        "times new roman", 12, "bold"), command=overview, width=23, height=2, padx=2, pady=6)
    f2_button3.grid(row=0, column=2)

    f2_button4 = Button(f2, text="Exit", font=(
        "times new roman", 12, "bold"), command=exit, width=23, height=2, padx=2, pady=6)
    f2_button4.grid(row=0, column=3)


def d1():
    screen4.destroy()


def userinfo():
    u1 = log_username.get()
    a = os.listdir()
    for i in a:
        if u1 == i:
            file = open(i, 'r')
            k = file.read()
            m = u1
            global screen4
            screen4 = Toplevel(screen)
            screen4.title("User info ")
            screen4.geometry("400x170")
            Label(screen4, text="Your username is"+":"+" "+m).pack()
            Label(screen4, text="").pack()
            Button(screen4, text="Return to account dashboard", command=d1).pack()
            file.close()


def gologin():
    u1 = log_username.get()
    u2 = log_password.get()
    a = os.listdir()
    for i in a:
        if i == u1:
            file = open(i, "r")
            file_data = file.read()
            file_data = file_data.split('\n')
            j = file_data[1]
            if u2 == j:
                screen2.destroy()
                screen3 = Toplevel(screen)
                screen3.title('Account Dashoard')
                screen3.geometry('600x300')
                Label(screen3, text="Welcome to your account dashboard"+" "+u1).pack()
                Label(screen3, text="").pack()
                Label(
                    screen3, text="Here is a list of things you might want to check out").pack()
                Label(screen3, text="").pack()
                Button(screen3, text="User details", width="15",
                       height="1", command=userinfo).pack()
                Label(screen3, text="").pack()
                Button(screen3, text="Event database", width="15",
                       height="1", command=maindatabase).pack()
                Label(screen3, text="").pack()
                Button(screen3, text="Contact an event manager",
                       height="1").pack()
                Label(screen3, text="").pack()
                Button(screen3, text="Issue a complaint", height="1").pack()
                return
            else:
                login_notif.config(
                    text="Password entered in incorrect", fg='red')
                return

        login_notif.config(
            text="No such account exists in the database", fg="red")


def login():
    global screen2
    global log_username
    global log_password
    global username_log
    global password_log
    global login_notif
    screen2 = Toplevel(screen)
    screen2.geometry('300x180')
    log_username = StringVar()
    log_password = StringVar()
    Label(screen2, text="Please enter details").pack()
    Label(text="").pack()
    Label(screen2, text="Username").pack()
    username_log = Entry(screen2, textvariable=log_username)
    username_log.pack()
    Label(screen2, text="Password").pack()
    password_log = Entry(screen2, textvariable=log_password, show='*')
    password_log.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width="10",
           height="1", command=gologin).pack()
    login_notif = Label(screen2)
    login_notif.pack()


Label(text="Please click on one of the below options to continue",
      font='16', width='300', height='2').pack()
Label(text="").pack()
Button(text="Login", height="3", width="30", command=login).pack()
Label(text="").pack()
Button(text="Register", height="3", width="30", command=register).pack()
screen.mainloop()
