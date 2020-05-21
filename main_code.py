import os, csv, logging
from random import randint, randrange
from tkinter import *
from tkinter import ttk,messagebox
import tkinter, logging, os, csv
import tkinter as tk
from tkcalendar import Calendar,DateEntry
import sqlite3,datetime
import itertools

def account_no_gen(user_name):

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    acc_no = ''

    for alpha in user_name:
        if (len(acc_no) < 12):
            if alpha in alphabets:
                index = alphabets.rfind(alpha)
                acc_no += str(index + 1)


            else:
                acc_no += '1'


        else:
            break


    if len(acc_no) > 12:
        final_acc_no = ''
        for index in acc_no:
            if len(final_acc_no) < 12:
                final_acc_no += index


        acc_no = final_acc_no
        return acc_no


    if len(acc_no) < 12:
        remain_index = 12 - len(acc_no)
        for index in range(remain_index):
            acc_no += str(randint(0,9))


        return acc_no


    else:
        return acc_no


class NewAccount:
    balance=0.00

    def __init__(self, Name, Fname, Email, Addr, City, Pc, State, Pan,Aadhar):
        logging.debug("creating a new account")
        self.full_name = Name
        self.father_name = Fname
        self.email=Email
        self.addr=Addr
        self.city=City
        self.pc=Pc
        self.state=State
        self.pan=Pan
        self.aadhar=Aadhar


    def get_account_no(self):
        if not ( self.full_name.isdigit()):
            name = self.full_name
            if name:
                logging.info("creating account number using name :{}".format(name))
                self.account_no = account_no_gen(name)
                return True


            else:
                logging.info('account number could not be created...')
                return False
        else:
            logging.warning("invalid Name : {}".format(self.full_name))
            return False

    def father(self):
        if self.father_name.isalpha():
            return self.father_name
        else :
            logging.warning("invalid Father Name : {}".format(self.father_name))
            return False

    def name(self):
        if not (self.full_name.isdigit()):
            return self.full_name
        else :
            logging.warning("invalid Address : {}".format(self.full_name))
            return False

    def email1(self):
        a="@gmail.com"
        if a in self.email:
            return self.email
        else:
            logging.warning("invalid Email : {}".format(self.email))
            return False

    def addr1(self):
        if not (self.addr.isdigit()):
            return self.addr
        else :
            logging.warning("invalid Address : {}".format(self.addr))
            return False

    def city1(self):
        if self.city.isalpha():
            return self.city
        else :
            logging.warning("invalid City : {}".format(self.city))
            return False

    def pc1(self):
        if (self.pc.isdigit()) and (len(self.pc)==6):
            return ("{}-{}-{}".format(self.pc[0:2], self.pc[2:3], self.pc[3:4]))
        else :
            logging.warning("invalid Pincode : {}".format(self.pc))
            return False


    def state1(self):
        if self.state.isalpha():
            return self.state
        else :
            logging.warning("invalid State : {}".format(self.state))
            return False

    def pan1(self):
        if (self.pan.isdigit()) and (len(self.pan)==10):
            return ("{}-{}-{}".format(self.pan[0:5], self.pan[5:9], self.pan[9]))

        else :
            logging.warning("invalid PAN Number : {}".format(self.pan))
            return False

    def aadhar1(self):
        if (self.aadhar.isdigit()) and (len(self.aadhar)==12):
            return ("{}-{}-{}".format(self.aadhar[0:5], self.aadhar[5:9], self.aadhar[9:11]))

        else :
            logging.warning("invalid Aadhar number : {}".format(self.aadhar))
            return False


def new_account():
    root.withdraw()
    new = Tk()
    new.title("WELCOME TO CREATE ACCOUNT CENTER")

    w, h = 1610, 900
    ws = new.winfo_screenwidth()
    hs = new.winfo_screenheight()
    x_axis = (ws/2) - (w/2)
    y_axis = (hs/2) - (h/2)

    new.geometry('%dx%d+%d+%d' % (w, h, x_axis, y_axis))
    new.resizable(0,0)

    def nexit():
         msg = messagebox.askquestion("CONFIRM","ARE YOU SURE YOU WANT TO EXIT?", icon='warning')
         if msg == "yes":

            new.withdraw()

            root.deiconify()

            logging.info('exiting window')


         else:
            logging.info('window still running')



    def createpin():


        pin= Tk()
        pin.title("WELCOME TO PIN CREATION CENTER")

        w, h = 1610, 900
        ws = pin.winfo_screenwidth()
        hs = pin.winfo_screenheight()
        x_axis = (ws/2) - (w/2)
        y_axis = (hs/2) - (h/2)

        pin.geometry('%dx%d+%d+%d' % (w, h, x_axis, y_axis))
        pin.resizable(0,0)

        def database(Pin1):

            Pin2=int(Pin1)
            Name2,Fname2,Email2,Addr2,City2,Pc2,State2=name.get(),fname.get(),email.get(),addr.get(),city.get(),pc.get(),state.get()
            Rlg2,Cate2,Income2,Edu2,Occu2,Pan2,Aadhar2=rlg.get(),cate.get(),income.get(),edu.get(),occu.get(),pan.get(),aadhar.get()
            Bd2,Bm2,By2=bd.get(),bm.get(),by.get()
            Gender2=gender.get()
            Status2=status.get()
            Scitizen2=scitizen.get()
            Exacc2=exacc.get()
            account_no=int(user.account_no)

            conn=sqlite3.connect('Python_ATM.db')
            c=conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS Customer_file(NAME text,FATHER_NAME text,BIRTH_DATE text,BIRTH_MONTH text,BIRTH_YEAR text,GENDER text,EMAIL text,MARITAL text,
                        ADDRESS text,CITY text,PIN_CODE text,STATE text,RELIGION text,CATEGORY text,INCOME text,EDU_QUALIFICATION text,OCCUPATION text,
                        PAN_CARD text,AADHAR text,SENIOR_CITIZEN text,EXISTING_ACCOUNT text,ACCOUNT_NO integer primary key,ACC_PIN integer,BALANCE real)''')



            c.execute('''insert into Customer_file(NAME,FATHER_NAME,BIRTH_DATE,BIRTH_MONTH,BIRTH_YEAR,GENDER,EMAIL,MARITAL,
                        ADDRESS,CITY,PIN_CODE,STATE,RELIGION,CATEGORY,INCOME,EDU_QUALIFICATION,OCCUPATION,PAN_CARD,AADHAR,
                        SENIOR_CITIZEN,EXISTING_ACCOUNT,ACCOUNT_NO,ACC_PIN,BALANCE) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(Name2,Fname2,Bd2,Bm2,By2,Gender2,Email2,Status2,Addr2,City2,Pc2,State2,Rlg2,Cate2,Income2,Edu2,Occu2,Pan2,Aadhar2,Scitizen2,Exacc2,account_no,Pin2,user.balance))

            conn.commit()
            conn.close()

        def finish():
            NAME=name.get()
            Pin1, V_Pin = CNID.get(), CCID.get()
            if (Pin1 == V_Pin) and (len(Pin1) == 4) and (Pin1.isdigit()):
                logging.info('pin matched successfully')
                logging.info('account no generated successfully')
                messagebox.showinfo('Confirmation', "Dear {}!  Your account is created successfully. Your account number is {}." .format(NAME,user.account_no))
                database(Pin1)
                pin.withdraw()
                root.deiconify()
                return


            else:
                logging.warning('pin did not match')
                messagebox.showwarning('Failed' ,"Your PIN did not match!, Try again! \n PIN must have exact 4 digits !!! ")


        def pclear():
            CNID.delete(0,END)
            CCID.delete(0,END)

        Label(pin,text="CREATE YOUR PIN HERE  !!!",font=("System",40)).place(x=445,y=180)

        def limitPin(*args):
            value = pinLimit.get()
            if len(value) > 4: pinLimit.set(value[:4])



        pinLimit = StringVar()
        pinLimit.trace('w', limitPin)

        def limitverPin(*args):
            value = pinverLimit.get()
            if len(value) > 4: pinverLimit.set(value[:4])



        pinverLimit = StringVar()
        pinverLimit.trace('w', limitPin)


        Label(pin,text="CREATE PIN     :",font=("Jokerman 22",32)).place(x=430,y=340)
        CNID= Entry(pin,  font=("Microsoft Himalaya", 38, "bold"),width=20,textvariable=pinLimit)
        CNID.place(x=850,y=340)

        Label(pin,text="CONFIRM PIN    :",font=("Jokerman 22",32)).place(x=430,y=440)
        CCID= Entry(pin,  font=("Microsoft Himalaya", 38, "bold"),width=20,textvariable=pinverLimit)
        CCID.place(x=850,y=440)

        Button(pin, text='CLEAR', bg='deep sky blue', font='Jokerman 22',bd="5",width=15,command=pclear).place(x=455,y=600)
        Button(pin, text='FINISH', bg='deep sky blue', font='Jokerman 22',bd="5",width=15,command=finish).place(x=915,y=600)


    def check():
        Name,Fname,Email,Addr,City,Pc,State=name.get(),fname.get(),email.get(),addr.get(),city.get(),pc.get(),state.get()
        Rlg,Cate,Income,Edu,Occu,Pan,Aadhar=rlg.get(),cate.get(),income.get(),edu.get(),occu.get(),pan.get(),aadhar.get()

        global user

        Bd,Bm,By=bd.get(),bm.get(),by.get()
        Gender=gender.get()
        Status=status.get()
        Scitizen=scitizen.get()
        Exacc=exacc.get()


        user =NewAccount(Name,Fname,Email,Addr,City,Pc,State,Pan,Aadhar)
        EMAIL,ADDR,CITY,PC,STATE,PAN,AADHAR=user.email1(),user.addr1(),user.city1(),user.pc1(),user.state1(),user.pan1(),user.aadhar1()
        FULL_NAME=user.name()
        FATHER=user.father()

        if not FULL_NAME:
            new.bell()
            logging.warn('user entered invalid FULL_NAME')
            messagebox.showwarning('Failed !!',"Invalid FULL_NAME !")

        elif not FATHER:
            new.bell()
            logging.warn('user entered invalid FATHER_NAME')
            messagebox.showwarning('Failed !!',"Invalid FATHER_NAME !")

        elif not Bd:
            new.bell()
            logging.warn('user entered invalid Birth Date')
            messagebox.showwarning('Failed !!',"Invalid Birth Date !")

        elif not Bm:
            new.bell()
            logging.warn('user entered invalid Birth Date')
            messagebox.showwarning('Failed !!',"Invalid Birth Date !")

        elif not By:
            new.bell()
            logging.warn('user entered invalid Birth Date')
            messagebox.showwarning('Failed !!',"Invalid Birth Date !")

        elif not Gender:
            new.bell()
            logging.warn('user entered invalid Gender')
            messagebox.showwarning('Failed !!',"Invalid Gender !")


        elif not EMAIL:
            new.bell()
            logging.warn('user entered invalid EMAIL')
            messagebox.showwarning('Failed !!', "Invalid Email !")

        elif not Status:
            new.bell()
            logging.warn('user entered invalid Marital status')
            messagebox.showwarning('Failed !!',"Invalid Marital Status !")


        elif not ADDR:
            new.bell()
            logging.warn('user entered invalid ADDRESS ')
            messagebox.showwarning('Failed !!', "Invalid Address!")

        elif not CITY:
            new.bell()
            logging.warn('user entered invalid CITY ')
            messagebox.showwarning('Failed !!', "Invalid City!")

        elif not PC:
            new.bell()
            logging.warn('user entered invalid Pincode ')
            messagebox.showwarning('Failed !!', "Invalid Pincode!")

        elif not STATE:
            new.bell()
            logging.warn('user entered invalid STATE ')
            messagebox.showwarning('Failed !!', "Invalid State!")

        elif not Rlg:
            new.bell()
            logging.warn('user entered invalid Religion')
            messagebox.showwarning('Failed !!',"Invalid Religion !")

        elif not Cate:
            new.bell()
            logging.warn('user entered invalid Category')
            messagebox.showwarning('Failed !!',"Invalid Category !")

        elif not Income:
            new.bell()
            logging.warn('user entered invalid Income')
            messagebox.showwarning('Failed !!',"Invalid Income !")

        elif not Edu:
            new.bell()
            logging.warn('user entered invalid Educational Qualification')
            messagebox.showwarning('Failed !!',"Invalid Educational Qualification !")

        elif not Occu:
            new.bell()
            logging.warn('user entered invalid Occupation')
            messagebox.showwarning('Failed !!',"Invalid Occupation !")

        elif not PAN:
            new.bell()
            logging.warn('user entered invalid PAN ')
            messagebox.showwarning('Failed !!', "Invalid Pan Card Number!")

        elif not AADHAR:
            new.bell()
            logging.warn('user entered invalid AADHAR ')
            messagebox.showwarning('Failed !!', "Invalid Aadhar Number!")

        elif not Scitizen:
            new.bell()
            logging.warn('User entered invalid Citizen status')
            messagebox.showwarning('Failed !!',"Invalid Citizen status")

        elif not Exacc:
            new.bell()
            logging.warn('User entered invalid existing acc status')
            messagebox.showwarning('Failed !!',"Invalid Existing account status")

        else:
            user.get_account_no()
            logging.info('user entered correct information and now prompting user for pin...')


            new.withdraw()
            createpin()



    Label(new,text="Page 1: Personal Details",font=("System",30)).place(x=150,y=50)
    Label(new,text="Page 2: Additional Details",font=("System",30)).place(x=950,y=50)
    Label(new,text="::",font=("System",30)).place(x=780,y=0)
    Label(new,text="::",font=("System",30)).place(x=780,y=50)
    Label(new,text="::",font=("System",30)).place(x=780,y=100)
    Label(new,text="::",font=("System",30)).place(x=780,y=150)
    Label(new,text="::",font=("System",30)).place(x=780,y=200)
    Label(new,text="::",font=("System",30)).place(x=780,y=250)
    Label(new,text="::",font=("System",30)).place(x=780,y=300)
    Label(new,text="::",font=("System",30)).place(x=780,y=350)
    Label(new,text="::",font=("System",30)).place(x=780,y=400)
    Label(new,text="::",font=("System",30)).place(x=780,y=450)
    Label(new,text="::",font=("System",30)).place(x=780,y=500)
    Label(new,text="::",font=("System",30)).place(x=780,y=550)
    Label(new,text="::",font=("System",30)).place(x=780,y=600)
    Label(new,text="::",font=("System",30)).place(x=780,y=650)
    Label(new,text="::",font=("System",30)).place(x=780,y=700)
    Label(new,text="::",font=("System",30)).place(x=780,y=750)
    Label(new,text="::",font=("System",30)).place(x=780,y=800)

    Label(new,text="Full Name :",font=("Jokerman 22",18)).place(x=70,y=140)
    name=Entry(new,width=23,font=("System",20))
    name.place(x=330,y=140)

    Label(new,text="Father Name :",font=("Jokerman 22",18)).place(x=70,y=210)
    fname=Entry(new,font=("System",22),width=23)
    fname.place(x=330,y=210)

    Label(new,text="Date Of Birth :",font=("Jokerman 22",18)).place(x=70,y=280)
    Label(new,text="Date",font=("System",17)).place(x=340,y=280)
    bd=ttk.Combobox(new,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15",
                                 "16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"],width=2,font=("System",15))
    bd.place(x=415,y=290)
    Label(new,text="Mon",font=("System",17)).place(x=460,y=280)
    bm=ttk.Combobox(new,values=["JAN","FEB","MAR","APRIL","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"],font=("System",12),width=3)
    bm.place(x=525,y=290)
    Label(new,text="Yr",font=("System",17)).place(x=580,y=280)
    by=ttk.Combobox(new,values=["1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990",
                                "1991","1992","1993","1994","1995","1996","1997","1998","1999","2000",
                                "2001","2002","2003","2004","2005","2006","2007","2008","2009","2010",
                                "2011","2012","2013","2014","2015","2016","2017","2018","2019","2020",
                                "2021","2022","2023","2024","2025","2026","2027","2028","2029","2030",
                                "2031","2032","2033","2034","2035","2036","2037","2038","2039","2040"],font=("System",15),width=4)
    by.place(x=620,y=290)


    Label(new,text="Gender :",font=("Jokerman 22",18)).place(x=70,y=350)
    gender=StringVar()
    Radiobutton(new, text="Male", variable=gender, value="Male", font=("System",23),width=5).place(x=320,y=350)
    Radiobutton(new, text="Female", variable=gender, value="Female", font=("System",23),width=5).place(x=450,y=350)
    Radiobutton(new, text="Other", variable=gender, value="Other", font=("System",23),width=5).place(x=570,y=350)
    gender.set("Male")

    Label(new,text="Email Address :",font=("Jokerman 22",18)).place(x=70,y=420)
    email=Entry(new,font=("System",20),width=23)
    email.place(x=330,y=420)

    Label(new,text="Marital Status :",font=("Jokerman 22",18)).place(x=70,y=490)
    status=StringVar()
    Radiobutton(new, text="Married", variable=status, value="Married", font=("System",23),width=7).place(x=320,y=490)
    Radiobutton(new, text="Unmarried", variable=status, value="Unmarrried", font=("System",23),width=7).place(x=500,y=490)
    status.set("Married")

    Label(new,text="Address :",font=("Jokerman 22",18)).place(x=70,y=560)
    addr=Entry(new,font=("System",20),width=23)
    addr.place(x=330,y=560)

    Label(new,text="City :",font=("Jokerman 22",18)).place(x=70,y=630)
    city=Entry(new,font=("System",22),width=23)
    city.place(x=330,y=630)

    Label(new,text="Pin Code :",font=("Jokerman 22",18)).place(x=70,y=700)
    pc=Entry(new,font=("System",22),width=23)
    pc.place(x=330,y=700)

    Label(new,text="State :",font=("Jokerman 22",18)).place(x=70,y=770)
    state=Entry(new,font=("System",22),width=23)
    state.place(x=330,y=770)

    Label(new,text="Religion :",font=("Jokerman 22",18)).place(x=870,y=140)
    rlg=ttk.Combobox(new,values=["Select","Hindu","Muslim","Christian","Sikh","Jewish","Others"],font=("System",22),width=22)
    rlg.place(x=1130,y=140)

    Label(new,text="Category :",font=("Jokerman 22",18)).place(x=870,y=210)
    cate=ttk.Combobox(new,values=["Select","General","OBC","SC","ST","SBC","Others"],font=("System",22),width=22)
    cate.place(x=1130,y=210)

    Label(new,text="Income :",font=("Jokerman 22",18)).place(x=870,y=280)
    income=ttk.Combobox(new,values=["Select","< 1,50,000","< 2,50,000","< 5,00,000","Upto 10,00,000","Above 10,00,000"],font=("System",22),width=22)
    income.place(x=1130,y=280)

    Label(new,text="Edu.Qualification :",font=("Jokerman 22",18)).place(x=870,y=350)
    edu=ttk.Combobox(new,values=["Select","Non-Graduate","Graduate","Post-Graduate","Doctrate","Others"],font=("System",22),width=22)
    edu.place(x=1130,y=350)

    Label(new,text="Occcupation :",font=("Jokerman 22",18)).place(x=870,y=420)
    occu=ttk.Combobox(new,values=["Select","Salaried","Self-Employed","Business","Student","Retired","Others"],font=("System",22),width=22)
    occu.place(x=1130,y=420)

    Label(new,text="PAN Number :",font=("Jokerman 22",18)).place(x=870,y=490)
    pan=Entry(new,font=("System",22),width=23)
    pan.place(x=1130,y=490)

    Label(new,text="Aadhar Number :",font=("Jokerman 22",18)).place(x=870,y=560)
    aadhar=Entry(new,font=("System",22),width=23)
    aadhar.place(x=1130,y=560)

    Label(new,text="Senior Citizen :",font=("Jokerman 22",18)).place(x=870,y=630)
    scitizen=StringVar()
    Radiobutton(new, text="Yes", variable=scitizen, value="YES", font=("System",23),width=7).place(x=1140,y=630)
    Radiobutton(new, text="No", variable=scitizen, value="NO", font=("System",23),width=7).place(x=1300,y=630)
    scitizen.set("YES")

    Label(new,text="Existing Account :",font=("Jokerman 22",18)).place(x=870,y=700)
    exacc=StringVar()
    e1=Radiobutton(new, text="Yes", variable=exacc, value="YES", font=("System",23),width=7)
    e1.place(x=1140,y=700)
    e2=Radiobutton(new, text="No", variable=exacc, value="NO", font=("System",23),width=7)
    e2.place(x=1300,y=700)
    exacc.set("YES")

    Button(new, text='BACK', bg='deep sky blue', font='Jokerman 22',bd="5",width=10,command=nexit).place(x=890,y=770)
    Button(new, text='NEXT', bg='deep sky blue', font='Jokerman 22',bd="5",width=10,command=check).place(x=1250,y=770)






def msg():
    messagebox.showinfo('All The Instructions are as follows:' ,
                        "\n 1. If you are reading this then it means that you have collected this project. "
                        "\n 2. Install Python3 on your system if you haven't already. "
                        " \n3. Install tkinter module in order to run the GUI of this program "
                        " \n4. If you are having any issues than please report it so we can fix it!"
                        "\n"
                        "\n"
                        "\n  This project made by Ganesh Gudewar & Shreyas Peherkar   ")

def log_check():
    PIN=int(pin.get())
    Id=int(id.get())
    conn=sqlite3.connect('Python_ATM.db')
    c=conn.cursor()
    c.execute("select ACCOUNT_NO from Customer_file where ACC_PIN=?",(PIN,))
    a=c.fetchall()
    conn.commit()
    conn.close()
    i=list(sum(a,()))
    if Id in i:
        m=i.index(Id)
        ID=i[m]
        login(ID)
    else:
        messagebox.showwarning('failed',"no such account !!")

def login(ID):

    ID1=ID

    def depo():

        work.withdraw()
        work1 = Tk()
        work1.title("WELCOME TO DEPOSIT CENTER")

        w, h = 1610, 900
        ws = work1.winfo_screenwidth()
        hs = work1.winfo_screenheight()
        x_axis = (ws/2) - (w/2)
        y_axis = (hs/2) - (h/2)

        work1.geometry('%dx%d+%d+%d' % (w, h, x_axis, y_axis))
        work1.resizable(0,0)

        def w1clear():
            dcash.delete(0,END)

        def w1exit():
         msg = messagebox.askquestion("CONFIRM","ARE YOU SURE YOU WANT TO EXIT?", icon='warning')
         if msg == "yes":

            work1.withdraw()

            work.deiconify()

            logging.info('exiting window')


         else:
            logging.info('window still running')

        def proceed():

            cashd=int(dcash.get())
            conn=sqlite3.connect('Python_ATM.db')
            c=conn.cursor()
            c.execute("select BALANCE from Customer_file where ACCOUNT_NO=?",(ID1,))
            money=c.fetchone()
            if cashd<=30000:
                money1=money[0]+cashd
                c.execute("update Customer_file SET BALANCE = ? where ACCOUNT_NO=? ",(money1,ID1))
                conn.commit()
                conn.close()
                messagebox.showinfo('Successfull !',"\n\n                <$> GS BANK <$>                \n\n           Your Transaction is sucessfully completed ...           \n           YOU DEPOSITED RS. {} IN {}           \n           Please check your balance..           \n           Your current BALANCE is RS. {}           \n\n\n            Thank you!! for using our ATM.....           \n\n\n\n".format(cashd,ID1,money1))
                work1.destroy()
                root.deiconify()
                id.delete(0,END)
                pin.delete(0,END)
            else:
                dcash.delete(0,END)
                messagebox.showwarning('Failed !!',"Your entered amount is greater than our Daily Deposit limit..!")

        Label(work1,text="MAXIMUM DAILY DEPOSIT LIMIT ", font=("System", 40)).place(x=370,y=100)
        Label(work1,text="  IS RS.30,000", font=("System", 40)).place(x=600,y=160)


        Label(work1,text=" PLZ ENTER YOUR AMOUNT ", font=("System", 40)).place(x=420,y=300)


        dcash= Entry(work1,  font=("Microsoft Himalaya", 38, "bold"),width=15)
        dcash.place(x=650,y=380)
        Button(work1, text='PROCEED', bg='deep sky blue', font='Jokerman 22',bd="5",width=15,command=proceed).place(x=430,y=470)
        Button(work1, text='CLEAR', bg='deep sky blue', font='Jokerman 22',bd="5",width=15,command=w1clear).place(x=890,y=470)
        Button(work1, text='BACK', bg='deep sky blue', font='Jokerman 22',bd="5",width=15,command=w1exit).place(x=650,y=620)


    def cash_wd():

        work.withdraw()
        work2 = Tk()
        work2.title("WELCOME TO WITHDRAWAL CENTER")

        w, h = 1610, 900
        ws = work2.winfo_screenwidth()
        hs = work2.winfo_screenheight()
        x_axis = (ws/2) - (w/2)
        y_axis = (hs/2) - (h/2)

        work2.geometry('%dx%d+%d+%d' % (w, h, x_axis, y_axis))
        work2.resizable(0,0)

        def w2clear():
            wcash.delete(0,END)

        def w2exit():
         msg = messagebox.askquestion("CONFIRM","ARE YOU SURE YOU WANT TO EXIT?", icon='warning')
         if msg == "yes":

            work2.withdraw()

            work.deiconify()

            logging.info('exiting window')


         else:
            logging.info('window still running')

        def collect():
            cashw=int(wcash.get())
            conn=sqlite3.connect('Python_ATM.db')
            c=conn.cursor()
            c.execute("select BALANCE from Customer_file where ACCOUNT_NO=?",(ID1,))
            money=c.fetchone()
            if cashw<=30000:
                if cashw <= money[0]:

                    money1=money[0]-cashw
                    c.execute("update Customer_file SET BALANCE = ? where ACCOUNT_NO=? ",(money1,ID1))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('Successfull !',"\n\n                <$> GS BANK <$>                \n\n           Your Transaction is sucessfully completed ...           \n            Please collect your cash RS. {}           \n            Your current balance is RS. {}           \n\n\n           Thank you!! for using our ATM           \n\n\n\n".format(cashw,money1))
                    work2.destroy()
                    root.deiconify()
                    id.delete(0,END)
                    pin.delete(0,END)

                else :
                    wcash.delete(0,END)
                    messagebox.showwarning('FAILED!!',"\n\n               Unable to proceed !!               \n               Please check your balance .....               \n\n")
            else:
                wcash.delete(0,END)
                messagebox.showwarning('Failed !!',"Your entered amount is greater than our Daily Withdrawal limit ..!")

        Label(work2,text="MAXIMUM DAILY WITHDRAWAL LIMIT ", font=("System", 40)).place(x=330,y=100)
        Label(work2,text="  IS RS.30,000", font=("System", 40)).place(x=620,y=160)


        Label(work2,text=" PLZ ENTER YOUR AMOUNT ", font=("System", 40)).place(x=420,y=300)


        wcash= Entry(work2,  font=("Microsoft Himalaya", 38, "bold"),width=15)
        wcash.place(x=650,y=380)
        Button(work2, text='COLLECT', bg='deep sky blue', font='Jokerman 22',bd="5",width=15,command=collect).place(x=430,y=470)
        Button(work2, text='CLEAR', bg='deep sky blue', font='Jokerman 22',bd="5",width=15,command=w2clear).place(x=890,y=470)
        Button(work2, text='BACK', bg='deep sky blue', font='Jokerman 22',bd="5",width=15,command=w2exit).place(x=650,y=620)


    def fast_cash():
        work.withdraw()
        work3 = Tk()
        work3.title("WELCOME TO TRANSACTION CENTER")

        w, h = 1610, 900
        ws = work3.winfo_screenwidth()
        hs = work3.winfo_screenheight()
        x_axis = (ws/2) - (w/2)
        y_axis = (hs/2) - (h/2)

        work3.geometry('%dx%d+%d+%d' % (w, h, x_axis, y_axis))
        work3.resizable(0,0)

        def w1():
            conn=sqlite3.connect('Python_ATM.db')
            c=conn.cursor()
            c.execute("select BALANCE from Customer_file where ACCOUNT_NO=?",(ID1,))
            money=c.fetchone()
            if 100 <= money[0]:

                money1=money[0]-100
                c.execute("update Customer_file SET BALANCE = ? where ACCOUNT_NO=? ",(money1,ID1))
                conn.commit()
                conn.close()
                messagebox.showinfo('Successfull !',"\n\n                <$> GS BANK <$>                \n\n           Your Transaction is sucessfully completed ...           \n            Please collect your cash RS. 100.00           \n            Your current balance is RS. {}           \n\n\n           Thank you!! for using our ATM           \n\n\n\n".format(money))
                work3.destroy()
                root.deiconify()
                id.delete(0,END)
                pin.delete(0,END)
            else :
                messagebox.showwarning('FAILED!!',"\n\n               Unable to proceed !!               \n               Please check your balance .....               \n\n")


        def w2():
            conn=sqlite3.connect('Python_ATM.db')
            c=conn.cursor()
            c.execute("select BALANCE from Customer_file where ACCOUNT_NO=?",(ID1,))
            money=c.fetchone()
            if 200 <= money[0]:

                money1=money[0]-200
                c.execute("update Customer_file SET BALANCE = ? where ACCOUNT_NO=? ",(money1,ID1))
                conn.commit()
                conn.close()
                messagebox.showinfo('Successfull !',"\n\n                 <$> GS BANK <$>                \n\n           Your Transaction is sucessfully completed ...           \n            Please collect your cash RS. 200.00           \n            Your current balance is RS. {}           \n\n\n           Thank you!! for using our ATM           \n\n\n\n".format(money))
                work3.destroy()
                root.deiconify()
                id.delete(0,END)
                pin.delete(0,END)
            else :
                messagebox.showwarning('FAILED!!',"\n\n               Unable to proceed !!               \n               Please check your balance .....               \n\n")

        def w3():
            conn=sqlite3.connect('Python_ATM.db')
            c=conn.cursor()
            c.execute("select BALANCE from Customer_file where ACCOUNT_NO=?",(ID1,))
            money=c.fetchone()
            if 500 <= money[0]:

                money1=money[0]-500
                c.execute("update Customer_file SET BALANCE = ? where ACCOUNT_NO=? ",(money1,ID1))
                conn.commit()
                conn.close()
                messagebox.showinfo('Successfull !',"\n\n                 <$> GS BANK <$>                \n\n           Your Transaction is sucessfully completed ...           \n            Please collect your cash RS. 500.00           \n            Your current balance is RS. {}           \n\n\n           Thank you!! for using our ATM           \n\n\n\n".format(money))
                work3.destroy()
                root.deiconify()
                id.delete(0,END)
                pin.delete(0,END)
            else :
                messagebox.showwarning('FAILED!!',"\n\n               Unable to proceed !!               \n               Please check your balance .....               \n\n")

        def w4():
            conn=sqlite3.connect('Python_ATM.db')
            c=conn.cursor()
            c.execute("select BALANCE from Customer_file where ACCOUNT_NO=?",(ID1,))
            money=c.fetchone()
            if 1000 <= money[0]:

                money1=money[0]-1000
                c.execute("update Customer_file SET BALANCE = ? where ACCOUNT_NO=? ",(money1,ID1))
                conn.commit()
                conn.close()
                messagebox.showinfo('Successfull !',"\n\n                 <$> GS BANK <$>                \n\n           Your Transaction is sucessfully completed ...           \n            Please collect your cash RS. 1000.00           \n            Your current balance is RS. {}           \n\n\n           Thank you!! for using our ATM           \n\n\n\n".format(money))
                work3.destroy()
                root.deiconify()
                id.delete(0,END)
                pin.delete(0,END)
            else :
                messagebox.showwarning('FAILED!!',"\n\n               Unable to proceed !!               \n               Please check your balance .....               \n\n")

        def w5():
            conn=sqlite3.connect('Python_ATM.db')
            c=conn.cursor()
            c.execute("select BALANCE from Customer_file where ACCOUNT_NO=?",(ID1,))
            money=c.fetchone()
            if 2000 <= money[0]:

                money1=money[0]-2000
                c.execute("update Customer_file SET BALANCE = ? where ACCOUNT_NO=? ",(money1,ID1))
                conn.commit()
                conn.close()
                messagebox.showinfo('Successfull !',"\n\n                 <$> GS BANK <$>                \n\n           Your Transaction is sucessfully completed ...           \n            Please collect your cash RS. 2000.00           \n            Your current balance is RS. {}           \n\n\n           Thank you!! for using our ATM           \n\n\n\n".format(money))
                work3.destroy()
                root.deiconify()
                id.delete(0,END)
                pin.delete(0,END)
            else :
                messagebox.showwarning('FAILED!!',"\n\n               Unable to proceed !!               \n               Please check your balance .....               \n\n")

        def w6():
            conn=sqlite3.connect('Python_ATM.db')
            c=conn.cursor()
            c.execute("select BALANCE from Customer_file where ACCOUNT_NO=?",(ID1,))
            money=c.fetchone()
            if 5000 <= money[0]:

                money1=money[0]-5000
                c.execute("update Customer_file SET BALANCE = ? where ACCOUNT_NO=? ",(money1,ID1))
                conn.commit()
                conn.close()
                messagebox.showinfo('Successfull !',"\n\n                 <$> GS BANK <$>                \n\n           Your Transaction is sucessfully completed ...           \n            Please collect your cash RS. 5000.00           \n            Your current balance is RS. {}           \n\n\n           Thank you!! for using our ATM           \n\n\n\n".format(money))
                work3.destroy()
                root.deiconify()
                id.delete(0,END)
                pin.delete(0,END)
            else :
                messagebox.showwarning('FAILED!!',"\n\n               Unable to proceed !!               \n               Please check your balance .....               \n\n")

        def w3exit():

         msg = messagebox.askquestion("CONFIRM","ARE YOU SURE YOU WANT TO EXIT?", icon='warning')
         if msg == "yes":

            work3.withdraw()

            work.deiconify()

            logging.info('exiting window')


         else:
            logging.info('window still running')



        Label(work3,text="PLZ SELECT YOUR CASH TYPE HERE ", font=("System", 40)).place(x=280,y=150)
        Button(work3, text='100 $', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=w1).place(x=310,y=270)
        Button(work3, text='200 $', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=w2).place(x=830,y=270)
        Button(work3, text='500 $', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=w3).place(x=310,y=420)
        Button(work3, text='1000 $', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=w4).place(x=830,y=420)
        Button(work3, text='2000 $', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=w5).place(x=310,y=570)
        Button(work3, text='5000 $', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=w6).place(x=830,y=570)
        Button(work3, text='EXIT', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=w3exit).place(x=600,y=730)


    def pinchange():

        work.withdraw()
        work4 = Tk()
        work4.title("WELCOME TO PINCHANGE CENTER")

        w, h = 1610, 900
        ws = work4.winfo_screenwidth()
        hs = work4.winfo_screenheight()
        x_axis = (ws/2) - (w/2)
        y_axis = (hs/2) - (h/2)

        work4.geometry('%dx%d+%d+%d' % (w, h, x_axis, y_axis))
        work4.resizable(0,0)

        def change():
            old=int(OID.get())
            new=int(NID.get())
            cnew=int(CID.get())
            conn=sqlite3.connect('Python_ATM.db')
            c=conn.cursor()
            c.execute("select ACC_PIN , BALANCE from Customer_file where ACCOUNT_NO=?",(ID1,))
            acc_pin=c.fetchone()
            if (old==acc_pin[0]) and (new == cnew):


                c.execute("update Customer_file SET ACC_PIN = ? where ACCOUNT_NO=? ",(new,ID1))
                conn.commit()
                conn.close()
                messagebox.showinfo('Successfull !',"\n\n                 <$> GS BANK <$>                \n\n           Your Updation is sucessfully completed ...           \n            Your new PIN is {}           \n            Your current balance is RS. {}           \n\n\n           Thank you!! for using our ATM           \n\n\n\n".format(new,acc_pin[1]))
                work4.destroy()
                root.deiconify()
                id.delete(0,END)
                pin.delete(0,END)
            else :
                OID.delete(0,END)
                NID.delete(0,END)
                CID.delete(0,END)
                messagebox.showwarning('FAILED!!'," Incurrect  PIN !!")


        def w4clear():
            OID.delete(0,END)
            NID.delete(0,END)
            CID.delete(0,END)

        def w4exit():

         msg = messagebox.askquestion("CONFIRM","ARE YOU SURE YOU WANT TO EXIT?", icon='warning')
         if msg == "yes":

            work4.withdraw()

            work.deiconify()

            logging.info('exiting window')


         else:
            logging.info('window still running')



        Label(work4,text="CHANGE YOUR PIN HERE  !!!",font=("System",40)).place(x=450,y=180)
        Label(work4,text="CURRENT PIN   :",font=("Jokerman 22",32)).place(x=340,y=300)
        OID= Entry(work4,  font=("Microsoft Himalaya", 38, "bold"),width=20)
        OID.place(x=750,y=300)

        Label(work4,text="NEW PIN            :",font=("Jokerman 22",32)).place(x=340,y=400)
        NID= Entry(work4,  font=("Microsoft Himalaya", 38, "bold"),width=20)
        NID.place(x=750,y=400)

        Label(work4,text="CONFIRM PIN    :",font=("Jokerman 22",32)).place(x=340,y=500)
        CID= Entry(work4,  font=("Microsoft Himalaya", 38, "bold"),width=20)
        CID.place(x=750,y=500)

        Button(work4, text='CHANGE', bg='deep sky blue', font='Jokerman 22',bd="5",width=15,command=change).place(x=480,y=620)
        Button(work4, text='CLEAR', bg='deep sky blue', font='Jokerman 22',bd="5",width=15,command=w4clear).place(x=940,y=620)
        Button(work4, text='BACK', bg='deep sky blue', font='Jokerman 22',bd="5",width=15,command=w4exit).place(x=700,y=770)

    def mini_statement():
        currentDT=datetime.datetime.now()
        date=currentDT.strftime("%Y/%M/%D")
        time=currentDT.strftime("%H:%M:%S")
        atm_no="SI100434898038"
        conn=sqlite3.connect('Python_ATM.db')
        c=conn.cursor()
        c.execute("select BALANCE from Customer_file where ACCOUNT_NO=?",(ID1,))
        money=c.fetchone()
        bal=money[0]
        messagebox.showinfo('MINI STATEMENT !!',"\n\n\n                <$> GS BANK <$>                \n\n\n        DATE    TIME    ATM NO.        \n      {}       {}      {}      \n\n        CARD NO.  **** **** **** ****      \n\n      TO KNOW YOUR BALANCE ,CALL TOLL FREE      \n      ON 1800-270-3333 FROM YOUR MOBILE AND      \n      GET YOUR ACCOUNT BALANCE INSTANTALY .      \n\n          AVAIL BAL    RS.     {}          \n\n      MAKE YOUR PURCHASES WITH GS BANK      \n      DEBIT CARDS.EARN FREEDOM POINTS AND      \n\n      GET FREE GIFTS.CALL 18002098500.      \n\n   For more info. Visit us at W.W.W.gsbank.com   \n\n".format(date,time,atm_no,bal))
        conn.commit()
        conn.close()
        work.destroy()
        root.deiconify()
        id.delete(0,END)
        pin.delete(0,END)

    def bal_check():
        conn=sqlite3.connect('Python_ATM.db')
        c=conn.cursor()
        c.execute("select NAME,BALANCE from Customer_file where ACCOUNT_NO=?",(ID1,))
        money=c.fetchone()
        customer=money[0]
        bal=money[1]
        messagebox.showinfo('<$> GS BANK <$>',"\n\n\n          Dear {} !           \n          IN YOUR ACC. {}          \n          YOUR CURRENT BALANCE IS RS. {}         \n                THANK YOU FOR USING OUR ATM              ".format(customer,ID1,bal))
        conn.commit()
        conn.close()
        work.destroy()
        root.deiconify()
        id.delete(0,END)
        pin.delete(0,END)

    def wexit():

         msg = messagebox.askquestion("CONFIRM","ARE YOU SURE YOU WANT TO EXIT?", icon='warning')
         if msg == "yes":

            work.withdraw()

            root.deiconify()

            logging.info('exiting window')


         else:
            logging.info('window still running')


    root.withdraw()
    work = Tk()
    work.title("WELCOME TO TRANSACTION CENTER")

    w, h = 1610, 900
    ws = work.winfo_screenwidth()
    hs = work.winfo_screenheight()
    x_axis = (ws/2) - (w/2)
    y_axis = (hs/2) - (h/2)

    work.geometry('%dx%d+%d+%d' % (w, h, x_axis, y_axis))
    work.resizable(0,0)

    Label(work,text="PLZ SELECT YOUR TRANSACTION HERE ", font=("System", 40)).place(x=280,y=150)
    Button(work, text='DEPOSIT', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=depo).place(x=310,y=270)
    Button(work, text='CASH WITHDRAWAL', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=cash_wd).place(x=830,y=270)
    Button(work, text='FAST CASH', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=fast_cash).place(x=310,y=420)
    Button(work, text='MINI STATEMENT', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=mini_statement).place(x=830,y=420)
    Button(work, text='BALANCE INQUIRY', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=bal_check).place(x=310,y=570)
    Button(work, text='PIN CHANGE', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=pinchange).place(x=830,y=570)
    Button(work, text='EXIT', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=wexit).place(x=600,y=730)



def rclean():
    id.delete(0,END)
    pin.delete(0,END)

root = Tk()
root.title("ATM Project")

w, h = 1610, 900
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x_axis = (ws/2) - (w/2)
y_axis = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x_axis, y_axis))
root.resizable(0,0)

menuBar = Menu()
root.config(menu = menuBar)

filemenu = Menu(menuBar, tearoff = 0)
filemenu.add_command(label = "New",command=new_account)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = quit)
menuBar.add_cascade(label = "File", menu = filemenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About",command=msg)
menuBar.add_cascade(label="Help", menu=helpMenu)

Label(root,text=" WELCOME TO GS ATM ", font=("System", 60)).place(x=430,y=150)
Label(root,text="Account No  : ", font=("System", 40, "bold")).place(x=400,y=280)
Label(root,text="Enter PIN     : ", font=("System", 40, "bold")).place(x=400,y=400)

id= Entry(root,  font=("Microsoft Himalaya", 32, "bold"),width=30)
id.place(x=800,y=300)
pin=Entry(root,  font=("Microsoft Himalaya", 32, "bold"),width=30)
pin.place(x=800,y=420)

Button(root, text='LOGIN', bg='deep sky blue', font='Jokerman 22',bd="5",width=12,command=log_check).place(x=800,y=540)
Button(root, text='CLEAR', bg='deep sky blue', font='Jokerman 22',bd="5",width=12,command=rclean).place(x=1040,y=540)
Button(root, text='CREATE NEW ACCOUNT', bg='deep sky blue', font='Jokerman 22',bd="5",width=26,command=new_account).place(x=800,y=640)


root.mainloop()

