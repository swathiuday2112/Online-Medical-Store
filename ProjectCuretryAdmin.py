import tkinter as tk
from tkinter.ttk import *
import mysql.connector
db = mysql.connector.connect(host="localhost", user="root", password="usrs123$",db ="curetry_new")
cursor = db.cursor()

r= tk.Tk()


class GUI():
    def create(self):
        r.geometry("500x500")
        r.title('Curetry')
        width= r.winfo_screenwidth() 
        height= r.winfo_screenheight()
        r.geometry("%dx%d" % (width, height))
        self.bg=tk.PhotoImage(file='sign.png')
        tk.Label(r,image=self.bg).place(relx=0.5, rely=0.5, anchor='center')
        label = tk.Label(text ="ADMIN CURETRY",font=('Courier New Baltic',50),bg='pink',fg='violet red')
        label.pack(pady = 10)

        r.configure(background='misty rose')
        tk.Label(r,text ="Enter details to proceed -",font=('Courier New Baltic',18),bg='misty rose',fg='violet red').place(x=650,y=150, anchor='center')
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        tk.Label(r, text ="USERNAME :" ,font=('Courier New Baltic',15),bg='misty rose',fg='violet red').place(x=520,y=480, anchor='center') 
        tk.Entry(r, textvariable =self.username ,font=('Courier New Baltic',15)).place(x=700, y=480, width = 200, height=26, anchor='center')  
        tk.Label(r, text ="PASSWORD :",font=('Courier New Baltic',15),bg='misty rose',fg='violet red').place(x=520,y=530, anchor='center') 
        tk.Entry(r, show='*', textvariable =self.password ,font=('Courier New Baltic',15)).place(x=700,y=530,  width = 200, height=26, anchor='center') 
        tk.Button(r, text ="Login",font=('Courier New Baltic',15),bg='violet red',fg='misty rose', command = self.check).place(x=640,y=580, anchor='center')

    def check(self):
        U = self.username.get();    P = self.password.get()
        cursor.execute('select * from admin');    x = cursor.fetchall()
        nw = tk.Toplevel(r);    nw.configure(background='misty rose')
        flag = 0 
        for row in x:
            if U==row[0] and P==row[1]:
                flag = 1
                nw.title("Welcome Screen")
                nw.geometry("275x200")
                tk.Button(nw, text="View Database",font=('Courier New Baltic',15),fg='misty rose',bg='violet red',command=lambda:[nw.destroy(),self.page()]).place(x=60,y=50)
                tk.Button(nw, text="Exit",font=('Courier New Baltic',15),fg='misty rose',bg='violet red',command=r.destroy).place(x=110,y=110)
                break
        if flag==0:
            nw.title("Message")
            nw.geometry("320x80")
            tk.Label(nw,text ="Invalid Username/Password",fg='red',font=15,bg='misty rose').place(x=25,y=25)

    def page(self):
        newWindow = tk.Toplevel(r)
        newWindow.title("CHOOSE")
        width= newWindow.winfo_screenwidth() 
        height= newWindow.winfo_screenheight()
        newWindow.geometry("%dx%d" % (width, height))
        label = tk.Label(newWindow,text ="Choose the Database!",font=('Courier New Baltic',50),bg='pink',fg='violet red')
        label.pack(pady = 10)
        newWindow.configure(background='misty rose')
        tk.Button(newWindow,text ="User Login Details",font=('Courier New Baltic',19),fg='misty rose',bg='violet red',command=self.deetslogin).place(relx=0.5,rely=0.4, anchor='center')
        tk.Button(newWindow,text ="Medicine Details",font=('Courier New Baltic',19),fg='misty rose',bg='violet red',command=lambda:[newWindow.destroy(),self.deetsmed()]).place(relx=0.5,rely=0.6, anchor='center')

    def deetslogin(self):
        newWindow2 = tk.Toplevel(r)
        newWindow2.title("User Login List")
        width= newWindow2.winfo_screenwidth() 
        height= newWindow2.winfo_screenheight()
        newWindow2.geometry("%dx%d" % (width, height))
        newWindow2.configure(background='misty rose')
        cursor.execute("select * from customer_details")
        x=cursor.fetchall()
        heading = (' '*28+'FIRST_NAME',' '*27+'LAST_NAME',' '*27+'EMAIL_ID',' '*27+'PASSWORD')
        x.insert(0,heading)
        i=0
        for y in x: 
            for j in range(len(y)):
                e = tk.Label(newWindow2,width=40, text=y[j],borderwidth=5,fg='black',bg='white',relief='ridge', anchor="w",font=('Courier New Baltic',10))
                e.grid(row=i, column=j) 
            i=i+1

    def deetsmed(self):
        global newWindow2
        newWindow2 = tk.Toplevel(r)
        newWindow2.title("Medicine List")
        width= newWindow2.winfo_screenwidth() 
        height= newWindow2.winfo_screenheight()
        newWindow2.geometry("%dx%d" % (width, height))
        newWindow2.configure(background='misty rose')
        cursor.execute("select name,type,quantity,price from med")
        x=cursor.fetchall()
        heading = (' '*30+'NAME', ' '*30+'TYPE', ' '*31+'QTY', ' '*27+'PRICE_1N_')
        x.insert(0,heading)
        i=0
        for y in x:
            for j in range(len(y)):
                e = tk.Label(newWindow2,width=40, text=y[j],borderwidth=5,fg='black',bg='white',relief='ridge', anchor="w",font=('Courier New Baltic',10))
                e.grid(row=i, column=j) 
            i=i+1
        tk.Button(newWindow2,text ="Edit Stocks",font=('Courier New Baltic',15),fg='misty rose',bg='violet red',command=self.manageStock).place(x=500,y=600, anchor='center')
        tk.Button(newWindow2,text ="Add Medicine",font=('Courier New Baltic',15),fg='misty rose',bg='violet red',command=self.addNewMedicine).place(x=680,y=600, anchor='center')
        tk.Button(newWindow2,text ="Exit",font=('Courier New Baltic',15),fg='misty rose',bg='violet red',command=r.destroy).place(x=830,y=600, anchor='center')

    def manageStock(self):
        nw = tk.Toplevel(r)
        nw.title("Manage Stocks")
        nw.geometry("550x250")
        nw.configure(background='misty rose')
        self.name = tk.StringVar()
        self.add = tk.StringVar()
        tk.Label(nw,text ="Enter Medicine Name : ",font=('Courier New Baltic',15),bg='pink',fg='violet red').place(x=20,y=50)
        tk.Entry(nw, textvariable=self.name ,font=('Courier New Baltic',15)).place(x=370, y=65, width = 260, anchor='center')
        tk.Label(nw,text ="ADD : ",font=('Courier New Baltic',15),bg='pink',fg='violet red').place(x=20,y=90)
        tk.Entry(nw, textvariable=self.add ,font=('Courier New Baltic',15)).place(x=290, y=105, width = 100, anchor='center')
        tk.Button(nw, text="Next",font=('Courier New Baltic',15),bg='violet red',fg='misty rose',command=lambda:[nw.destroy(),self.ADDQTY()]).place(x=250,y=160)

    def ADDQTY(self):
        MN = self.name.get()
        Addqty = self.add.get()
        command = 'select name from med where name= "%s"'%(MN)
        cursor.execute(command); x=cursor.fetchall()
        nw = tk.Toplevel(r)
        nw.title("Message")
        nw.geometry("280x280")
        nw.configure(background='misty rose')
        if x==[]:
            tk.Label(nw, text ="Medicine Not Found! ",font=('Courier New Baltic',15),bg='pink',fg='violet red').place(x=20,y=50)
            tk.Button(nw, text="Edit Stocks",font=('Courier New Baltic',15),bg='violet red',fg='misty rose',command=lambda:[nw.destroy(),self.manageStock()]).place(x=20,y=100)
            tk.Button(nw, text="Exit",font=('Courier New Baltic',15),bg='violet red',fg='misty rose',command=r.destroy).place(x=20,y=160)
        
        else:
            cmd = 'update med set quantity=quantity+ %s where name = "%s" '%(Addqty,MN)
            cursor.execute(cmd); db.commit()
            tk.Label(nw,text ="MODIFIED! ",font=('Courier New Baltic',15),bg='pink',fg='violet red').place(x=20,y=30)
            tk.Button(nw, text="Edit Stocks",font=('Courier New Baltic',15),bg='violet red',fg='misty rose',command=lambda:[nw.destroy(),self.manageStock()]).place(x=20,y=90)
            tk.Button(nw, text="Main Page",font=('Courier New Baltic',15),bg='violet red',fg='misty rose',command=lambda:[nw.destroy(),newWindow2.destroy(),self.page()]).place(x=20,y=155)
            tk.Button(nw, text="Exit",font=('Courier New Baltic',15),bg='violet red',fg='misty rose',command=r.destroy).place(x=20,y=220)

    def addNewMedicine(self):
        nw = tk.Toplevel(r)
        nw.title("Add New Medicine")
        nw.geometry("550x280")
        nw.configure(background='misty rose')
        self.name = tk.StringVar()
        self.type = tk.StringVar()
        self.price = tk.StringVar()
        self.setqty = tk.StringVar()
        tk.Label(nw,text ="Enter Medicine Name : ",font=('Courier New Baltic',15),bg='pink',fg='violet red').place(x=20,y=50)
        tk.Entry(nw, textvariable=self.name ,font=('Courier New Baltic',15)).place(x=350, y=65, width = 200, anchor='center')
        tk.Label(nw,text ="Enter Type : ",font=('Courier New Baltic',15),bg='pink',fg='violet red').place(x=20,y=90)
        tk.Entry(nw, textvariable=self.type,font=('Courier New Baltic',15)).place(x=350, y=105, width = 200, anchor='center')
        tk.Label(nw,text ="Enter Price(1unit) : ",font=('Courier New Baltic',15),bg='pink',fg='violet red').place(x=20,y=130)
        tk.Entry(nw, textvariable=self.price ,font=('Courier New Baltic',15)).place(x=350, y=145, width = 200, anchor='center')
        tk.Label(nw,text ="Set Quantity to - ",font=('Courier New Baltic',15),bg='pink',fg='violet red').place(x=20,y=170)
        tk.Entry(nw, textvariable=self.setqty ,font=('Courier New Baltic',15)).place(x=350, y=185, width = 200, anchor='center')
        tk.Button(nw, text="Submit",font=('Courier New Baltic',15),bg='violet red',fg='misty rose',command=lambda:[nw.destroy(),self.ANMsubmit()]).place(x=250,y=220)

    def ANMsubmit(self):
        medname = self.name.get(); MEDNAME = medname.title()
        medtype = self.type.get(); MEDTYPE = medtype.title()
        MEDPRICE = self.price.get(); SETQTY = self.setqty.get()
        cmd = 'insert into med(name,type,quantity,price) values( "%s", "%s", %s, %s)'%(MEDNAME,MEDTYPE,SETQTY,MEDPRICE)
        cursor.execute(cmd); db.commit()
        nw = tk.Toplevel(r)
        nw.title("Message")
        nw.geometry("280x300")
        nw.configure(background='misty rose')
        tk.Label(nw,text ="Succesfully Added! ",font=('Courier New Baltic',15),bg='pink',fg='violet red').place(x=20,y=30)
        tk.Button(nw, text="Any More New MED?",font=('Courier New Baltic',15),bg='violet red',fg='misty rose',command=lambda:[nw.destroy(),self.addNewMedicine()]).place(x=20,y=90)
        tk.Button(nw, text="Main Page",font=('Courier New Baltic',15),bg='violet red',fg='misty rose',command=lambda:[nw.destroy(),self.page()]).place(x=20,y=160)
        tk.Button(nw, text="Exit",font=('Courier New Baltic',15),bg='violet red',fg='misty rose',command=r.destroy).place(x=20,y=230)
    
if __name__ == '__main__':
    GUI().create()
