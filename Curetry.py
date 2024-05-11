from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import mysql.connector
from PIL import ImageTk, Image
import math
from fpdf import FPDF
import datetime

sqlobj = mysql.connector.connect(host='localhost',user='root',
                                 password='usrs123$',database='curetry_new')
cur = sqlobj.cursor()

r = tk.Tk()

CART = []
class GUI():
    def createUI(self):
        r.geometry("500x500"); r.title('Curetry')
        r.configure(background='pink')
        width= r.winfo_screenwidth()
        height= r.winfo_screenheight()
        r.geometry("%dx%d" % (width, height))
        self.bg=tk.PhotoImage(file='logo.png')
        tk.Label(r,image=self.bg).place(relx=0.5, rely=0.5, anchor='center')
        tk.Label(text ="WELCOME TO CURETRY",font=('Courier New Baltic',50),bg='pink',fg='violet red').pack(pady = 10)
        tk.Button(r, text='LOG IN', command=self.login,bg='violet red',fg='pink',font=('Courier New Baltic',15)).place(relx=0.5, rely=0.75, anchor='center')
        tk.Button(r, text='SIGN UP',command=self.signup,bg='violet red',fg='pink',font=('Courier New Baltic',15)).place(relx=0.5, rely=0.82, anchor='center')

    def login(self):
        global newWindow1
        newWindow1 = tk.Toplevel(r)
        newWindow1.title("Login");    newWindow1.geometry("300x300")
        newWindow1.configure(background='misty rose')
        tk.Label(newWindow1,text ="Enter login details :",font=('Courier New Baltic',20),bg='misty rose',fg='violet red').pack()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        tk.Label(newWindow1,text='Email Id:',font=('Courier New Baltic',12),bg='misty rose',fg='violet red').place(x=40,y=60)
        tk.Entry(newWindow1,textvariable=self.username, font=('calibre',10,'normal')).place(x=130,y=60)
        tk.Label(newWindow1,text='Password:',font=('Courier New Baltic',12),bg='misty rose',fg='violet red').place(x=40,y=100)
        tk.Entry(newWindow1,show='*',textvariable=self.password, font=('calibre',10,'normal')).place(x=130,y=100)
        tk.Button(newWindow1, text = "Submit",bg='violet red',fg='misty rose',width=10,command=self.checkEntry).place(x=40,y=190)
        tk.Button(newWindow1, text = "Exit",bg='violet red',fg='misty rose',width=10,command = r.destroy).place(x=40,y=230)

    def signup(self):
        global newWindow2
        newWindow2 = tk.Toplevel(r); newWindow2.title("Sign Up")
        newWindow2.geometry("500x500")
        newWindow2.configure(background='misty rose')
        tk.Label(newWindow2,text ="Please fill the required fields.",font=('Courier New Baltic',20),bg='misty rose',fg='violet red').place(x=60,y=100)
        self.first = tk.StringVar()
        self.last = tk.StringVar()
        self.mail = tk.StringVar()
        self.password = tk.StringVar()
        self.cpwd = tk.StringVar()
        tk.Label(newWindow2,text='First Name:',font=('Courier New Baltic',12),bg='misty rose',fg='violet red').place(x=60,y=180)
        tk.Entry(newWindow2,textvariable=self.first, font=('calibre',10,'normal')).place(x=310,y=180)
        tk.Label(newWindow2,text='Last Name:',font=('Courier New Baltic',12),bg='misty rose',fg='violet red').place(x=60,y=210)
        tk.Entry(newWindow2,textvariable=self.last, font=('calibre',10,'normal')).place(x=310,y=210)
        tk.Label(newWindow2,text='Email Id:',font=('Courier New Baltic',12),bg='misty rose',fg='violet red').place(x=60,y=240)
        tk.Entry(newWindow2,textvariable=self.mail, font=('calibre',10,'normal')).place(x=310,y=240)
        tk.Label(newWindow2,text='Set Up A Password:',font=('Courier New Baltic',12),bg='misty rose',fg='violet red').place(x=60,y=270)
        tk.Entry(newWindow2,show='*',textvariable=self.password, font=('calibre',10,'normal')).place(x=310,y=270)
        tk.Label(newWindow2,text='Confirm Password:',font=('Courier New Baltic',12),bg='misty rose',fg='violet red').place(x=60,y=300)
        tk.Entry(newWindow2,show='*',textvariable=self.cpwd, font=('calibre',10,'normal')).place(x=310,y=300)
        tk.Button(newWindow2, text = "Submit",bg='violet red',fg='misty rose',width=10,command = self.submitact).place(x=200,y=350)
        tk.Button(newWindow2, text = "Exit",bg='violet red',fg='misty rose',width=10,command = r.destroy).place(x=200,y=390)

    def checkEntry(self):
        getUsername = self.username.get()
        getPassword = self.password.get()
        cmd='''select first_name from customer_details where email in ("%s") and
           password in ("%s")'''%(getUsername,getPassword)
        cur.execute(cmd); T=cur.fetchall()
        nw3 = tk.Toplevel(r); nw3.configure(background='misty rose')
        if T==[]:
            nw3.title("Message"); nw3.geometry("310x70")
            tk.Label(nw3,text ="Invalid Email Id/Password",fg='red',bg='misty rose',font=3).place(x=30,y=20)            
        else:
            newWindow1.destroy()
            name = T[0][0].title()
            nw3.title("Welcome Screen"); nw3.geometry("290x220")
            tk.Label(nw3,text ="Hi "+name+'!',bg='misty rose',fg='violet red',font=3).place(x=20,y=20)
            tk.Label(nw3,text ="Order Medicines With\n Exiting Offers!",fg='blue',bg='misty rose',font=3).place(x=40,y=70)
            tk.Button(nw3, text="Order Now",bg='violet red',fg='pink',font=3,command=lambda:[nw3.destroy(),self.order()]).place(x=85,y=150)

    def submitact(self):
        first=self.first.get();  last=self.last.get();  email=self.mail.get()
        password=self.password.get();  cpwd=self.cpwd.get()
        nw4 = tk.Toplevel(r)
        nw4.configure(background='misty rose')
        if first=='' or last=='' or email=='' or password=='' or cpwd=='':
            nw4.title("Pop Up"); nw4.geometry("230x80")
            tk.Label(nw4,text ="WARNING\nField(s) Can't Be Empty!",font=('Courier New Baltic',10),bg='misty rose',fg='red').place(x=40,y=20)

        elif password!=cpwd:
            nw4.title("Pop Up"); nw4.geometry("150x60")
            tk.Label(nw4,text ="Confirm Password\n Doesn't Match!",font=('Courier New Baltic',10),bg='misty rose',fg='red').place(x=20,y=15)
            
        else:
            newWindow2.destroy()
            sql="INSERT INTO customer_details(First_Name,Last_Name,email,password)VALUES(%s,%s,%s,%s)"
            rows = (first,last,email,password); cur.execute(sql, rows)
            sqlobj.commit()
            nw4.title("Welcome Screen"); nw4.geometry("200x200")
            tk.Label(nw4,text ="Hi "+first.title()+'!').place(x=20,y=20)
            tk.Label(nw4,text ="Order Medicines With\n Exiting Offers!",fg='blue').place(x=40,y=70)
            tk.Button(nw4, text="Order Now",command=lambda:[nw4.destroy(),self.order()]).place(x=60,y=130)
            
    
    def order(self):
        root = tk.Toplevel(r)
        root.title("Order Page")
        width= root.winfo_screenwidth() 
        height= root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        root.configure(background='misty rose')
        global a,b,c,d,e,f,g,h,i,j,k,l

        image = Image.open('1.png').resize((150,150))
        self.my_img = ImageTk.PhotoImage(image)
        a = 'Uniclave 650mg' 
        tk.Button(root,image = self.my_img,command = lambda:[root.destroy(),self.imgButton(a)]).place(x=50,y=50)
        tk.Label(root,text=a,bg='misty rose',fg='violet red').place(x=50,y=210)
        tk.Label(root,text='Rs 16.75',bg='misty rose',fg='violet red').place(x=50,y=235)

        image1 = Image.open('10.png').resize((150,150))
        self.my_img1 = ImageTk.PhotoImage(image1)
        b = 'Benedryl-Dry'
        tk.Button(root,image = self.my_img1,command = lambda:[root.destroy(),self.imgButton(b)]).place(x=250,y=50)
        tk.Label(root,text=b,bg='misty rose',fg='violet red').place(x=250,y=210)
        tk.Label(root,text='Rs 130.00',bg='misty rose',fg='violet red').place(x=250,y=235)

        image2 = Image.open('11.png').resize((150,150))
        self.my_img2 = ImageTk.PhotoImage(image2)
        c = 'Concor'
        tk.Button(root,image = self.my_img2,command = lambda:[root.destroy(),self.imgButton(c)]).place(x=450,y=50)
        tk.Label(root,text=c,bg='misty rose',fg='violet red').place(x=450,y=210)
        tk.Label(root,text='Rs 20.00',bg='misty rose',fg='violet red').place(x=450,y=235)

        image3 = Image.open('2.png').resize((150,150))
        self.my_img3 = ImageTk.PhotoImage(image3)
        d = 'Paracetamol'
        tk.Button(root,image = self.my_img3,command = lambda:[root.destroy(),self.imgButton(d)]).place(x=650,y=50)
        tk.Label(root,text=d,bg='misty rose',fg='violet red').place(x=650,y=210)
        tk.Label(root,text='Rs 17.50',bg='misty rose',fg='violet red').place(x=650,y=235)

        image4 = Image.open('3.png').resize((150,150))
        self.my_img4= ImageTk.PhotoImage(image4)
        e = 'Dolo-650'
        tk.Button(root,image = self.my_img4,command = lambda:[root.destroy(),self.imgButton(e)]).place(x=850,y=50)
        tk.Label(root,text=e,bg='misty rose',fg='violet red').place(x=850,y=210)
        tk.Label(root,text='Rs 15.00',bg='misty rose',fg='violet red').place(x=850,y=235)

        image5 = Image.open('4.png').resize((150,150))
        self.my_img5 = ImageTk.PhotoImage(image5)
        f = 'Zincovit' 
        tk.Button(root,image = self.my_img5,command = lambda:[root.destroy(),self.imgButton(f)]).place(x=1050,y=50)
        tk.Label(root,text=f,bg='misty rose',fg='violet red').place(x=1050,y=210)
        tk.Label(root,text='Rs 10.00',bg='misty rose',fg='violet red').place(x=1050,y=235)

        image6 = Image.open('5.png').resize((150,150))
        self.my_img6 = ImageTk.PhotoImage(image6)
        g = 'Fluticone'
        tk.Button(root,image = self.my_img6,command = lambda:[root.destroy(),self.imgButton(g)]).place(x=50,y=300)
        tk.Label(root,text=g,bg='misty rose',fg='violet red').place(x=50,y=460)
        tk.Label(root,text='Rs 297.45',bg='misty rose',fg='violet red').place(x=50,y=485)

        image7 = Image.open('6.png').resize((150,150))
        self.my_img7 = ImageTk.PhotoImage(image7)
        h = 'Crocin'
        tk.Button(root,image = self.my_img7,command = lambda:[root.destroy(),self.imgButton(h)]).place(x=250,y=300)
        tk.Label(root,text=h,bg='misty rose',fg='violet red').place(x=250,y=460)
        tk.Label(root,text='Rs 100.99',bg='misty rose',fg='violet red').place(x=250,y=485)

        image8 = Image.open('7.png').resize((150,150))
        self.my_img8 = ImageTk.PhotoImage(image8)
        i = 'Montek 10mg'
        tk.Button(root,image = self.my_img8,command = lambda:[root.destroy(),self.imgButton(i)]).place(x=450,y=300)
        tk.Label(root,text=i,bg='misty rose',fg='violet red').place(x=450,y=460)
        tk.Label(root,text='Rs 23.00',bg='misty rose',fg='violet red').place(x=450,y=485)

        image9 = Image.open('8.png').resize((150,150))
        self.my_img9 = ImageTk.PhotoImage(image9)
        j = 'Montek 20mg'
        tk.Button(root,image = self.my_img9,command = lambda:[root.destroy(),self.imgButton(j)]).place(x=650,y=300)
        tk.Label(root,text=j,bg='misty rose',fg='violet red').place(x=650,y=460)
        tk.Label(root,text='Rs 38.00',bg='misty rose',fg='violet red').place(x=650,y=485)

        image10 = Image.open('9.png').resize((150,150))
        self.my_img10 = ImageTk.PhotoImage(image10)
        k = 'Levolin'
        tk.Button(root,image = self.my_img10,command = lambda:[root.destroy(),self.imgButton(k)]).place(x=850,y=300)
        tk.Label(root,text=k,bg='misty rose',fg='violet red').place(x=850,y=460)
        tk.Label(root,text='Rs 225.00',bg='misty rose',fg='violet red').place(x=850,y=485)
        
        image11 = Image.open('12.png').resize((150,150))
        self.my_img11 = ImageTk.PhotoImage(image11)
        l = 'Dexorange' 
        tk.Button(root,image = self.my_img11,command = lambda:[root.destroy(),self.imgButton(l)]).place(x=1050,y=300)
        tk.Label(root,text=l,bg='misty rose',fg='violet red').place(x=1050,y=460)
        tk.Label(root,text='Rs 160.00',bg='misty rose',fg='violet red').place(x=1050,y=485)
        
        self.name = tk.StringVar()
        tk.Label(root,text='Medicine Name:',font=('Courier New Baltic',12),bg='misty rose',fg='violet red').place(x = 500, y = 525)
        tk.Entry(root,textvariable=self.name, font=('calibre',10,'normal')).place(x = 650, y = 525)
        tk.Button(root, text = "Search",bg='violet red',fg='misty rose',width=10,command = lambda:[root.destroy(),self.search()]).place(x = 630, y = 570)
    
    def search(self):
        global medName; medName = self.name.get().title()
        sql = "select name,type,quantity,price from med where name = ('%s')"%(medName)
        cur.execute(sql);   T=cur.fetchall()
        nw = tk.Toplevel(r);    nw.configure(background='misty rose')
        if T==[]:
            nw.title("Message");    nw.geometry("260x180")
            tk.Label(nw,text ="Medicine Not Available",fg='red',bg='misty rose',font=15).place(x=45,y=20)            
            tk.Button(nw,text = "Search Med", fg='misty rose', bg='violet red',font=8, command=lambda:[nw.destroy(),self.order()]).place(x=80,y=60)
            if CART!=[]: tk.Button(nw,text = "View Bill", fg='misty rose', bg='violet red',font=8, command=lambda:[nw.destroy(),self.bill()]).place(x=90,y=113)
            else: tk.Button(nw,text = "Exit", fg='misty rose', bg='violet red',font=8, command=r.destroy).place(x=107,y=113)
        else:
            nw.title("Medicine Details");   nw.geometry("500x250")
            medType = T[0][1]
            global avlqty; avlqty = T[0][2]
            global price; price = T[0][3]
            tk.Label(nw, text="MEDICINE NAME:", font=('Courier New Baltic',12),fg='violet red',bg='misty rose').place(x=25,y=20)
            tk.Label(nw, text=medName, font=('Courier New Baltic',12),fg='black',bg='misty rose').place(x=200,y=20)
            tk.Label(nw, text="TYPE:", font=('Courier New Baltic',12),fg='violet red',bg='misty rose').place(x=25,y=60)
            tk.Label(nw, text=medType, font=('Courier New Baltic',12),fg='black',bg='misty rose').place(x=200,y=60)
            tk.Label(nw, text="PRICE PER UNIT:", font=('Courier New Baltic',12),fg='violet red',bg='misty rose').place(x=25,y=100)
            tk.Label(nw, text=price, font=('Courier New Baltic',12),fg='black',bg='misty rose').place(x=200,y=100)
            self.qSelection = tk.IntVar()
            tk.Label(nw,text='QUANTITY:',font=('Courier New Baltic',12),bg='misty rose',fg='violet red').place(x=25,y=140)
            drop=OptionMenu(nw,self.qSelection,"Select",1,2,3,4,5,6,7,8,9,10).place(x=200,y=140)
            tk.Button(nw, text = "Add To Cart",bg='violet red',fg='misty rose',width=10,command = lambda:[nw.destroy(),self.addToCart()]).place(x=200,y=180)

    def imgButton(self,imgName):
        sql = "select name,type,quantity,price from med where name = '%s' "%(imgName)
        global img_name
        img_name = imgName        
        cur.execute(sql);   T=cur.fetchall()
        nw = tk.Toplevel(r);    nw.configure(background='misty rose')
        nw.title("Medicine Details");   nw.geometry("400x250")
        medType = T[0][1]
        global avlqty; avlqty = T[0][2]
        global price; price = T[0][3]
        tk.Label(nw, text="MEDICINE NAME:", font=('Courier New Baltic',12),fg='violet red',bg='misty rose').place(x=25,y=20)
        tk.Label(nw, text=img_name, font=('Courier New Baltic',12),fg='black',bg='misty rose').place(x=200,y=20)
        tk.Label(nw, text="TYPE:", font=('Courier New Baltic',12),fg='violet red',bg='misty rose').place(x=25,y=60)
        tk.Label(nw, text=medType, font=('Courier New Baltic',12),fg='black',bg='misty rose').place(x=200,y=60)
        tk.Label(nw, text="PRICE PER UNIT:", font=('Courier New Baltic',12),fg='violet red',bg='misty rose').place(x=25,y=100)
        tk.Label(nw, text=price, font=('Courier New Baltic',12),fg='black',bg='misty rose').place(x=200,y=100)
        self.qSelection = tk.IntVar()
        tk.Label(nw,text='QUANTITY:',font=('Courier New Baltic',12),bg='misty rose',fg='violet red').place(x=25,y=140)
        drop=OptionMenu(nw,self.qSelection,"Select",1,2,3,4,5,6,7,8,9,10).place(x=200,y=140)
        tk.Button(nw, text = "Add To Cart",bg='violet red',fg='misty rose',width=10,command = lambda:[nw.destroy(),self.addToCart()]).place(x=200,y=180)
        
    def addToCart(self): 
        nw7 = tk.Toplevel(r); nw7.configure(background='misty rose')
        qty = self.qSelection.get()
        if qty > avlqty:
            nw7.title('Message'); nw7.geometry("280x180")
            tk.Label(nw7, text='Sorry! Stock not available', font=('Courier New Baltic',15),fg='red', bg='misty rose').place(x=25,y=20)
            tk.Button(nw7,text = "Search Med", fg='misty rose', bg='violet red',font=8, command=lambda:[nw7.destroy(),self.order()]).place(x=87,y=70)
            if CART!=[]: tk.Button(nw7,text = "View Bill", fg='misty rose', bg='violet red',font=8, command=lambda:[nw7.destroy(),self.bill()]).place(x=97,y=120)
            else: tk.Button(nw7,text = "Exit", fg='misty rose', bg='violet red',font=8, command=r.destroy).place(x=112,y=120)
        else:
            nw7.title("Qty"); nw7.geometry("250x200")
            medName = self.name.get().title()
            if medName=='': medName = img_name
            cur.execute('update med set quantity=quantity- %s where name = "%s"'%(qty,medName))
            sqlobj.commit()
            totalPrice = math.ceil(price*qty)
            L = [medName, qty, float(totalPrice)]            
            CART.append(L)
            tk.Label(nw7, text='Added To Cart!', font=('Courier New Baltic',15),fg='blue',bg='misty rose').place(x=50,y=20)
            tk.Button(nw7, text='Order More',bg='violet red',fg='misty rose',width=10,command = lambda:[nw7.destroy(), self.order()]).place(x=80,y=80)
            tk.Button(nw7, text='Bill',bg='violet red',fg='misty rose',width=10,command = lambda:[nw7.destroy(), self.bill()]).place(x=80,y=130)

    def bill(self):
        nw8 = tk.Toplevel(r); nw8.title("BILL")
        nw8.configure(background='misty rose')
        nw8.geometry("680x500")
        heading = (' '*5+'MEDICINE NAME',' '*10+'QUANTITY',' '*12+'AMOUNT')
        empty = ('','','')
        CART.insert(0,empty); CART.insert(0,heading)
        i=0
        for y in CART:
            if y == CART[0]:
                for j in range(len(y)):
                    e = tk.Label(nw8,width=20, text=y[j],borderwidth=2,fg='black',bg='white',relief='ridge', anchor="w",font=('Courier New Baltic',15))
                    e.grid(row=i, column=j)
            else:
                for j in range(len(y)):
                    e = tk.Label(nw8,width=20, text=y[j],borderwidth=2,fg='violet red',bg='white',relief='ridge', anchor="w",font=('Courier New Baltic',15))
                    e.grid(row=i, column=j) 
            i=i+1
            
        length = len(CART); height = 30*length

        global tot,gst
        tot = 0
        for row in CART[2:] : tot+=row[2]
        gst = math.ceil(0.18*tot)
        tk.Label(nw8, text='TOTAL:', font=('Courier New Baltic',12),fg='violet red',bg='misty rose').place(x=50,y=height+50)
        tk.Label(nw8, text='₹'+str(int(tot)), font=('Courier New Baltic',12),fg='violet red',bg='misty rose').place(x=455,y=height+50)
        tk.Label(nw8, text='GST(18%) : ', font=('Courier New Baltic',12),fg='violet red',bg='misty rose').place(x=50,y=(height+80))
        tk.Label(nw8, text='₹'+str(gst)  , font=('Courier New Baltic',12),fg='violet red',bg='misty rose').place(x=455,y=(height+80))
        tk.Label(nw8, text='SHIPPING CHARGES:', font=('Courier New Baltic',12),fg='violet red',bg='misty rose').place(x=50,y=(height+110))
        tk.Label(nw8, text='₹50', font=('Courier New Baltic',12),fg='violet red',bg='misty rose').place(x=455,y=(height+110))
        tk.Label(nw8, text='-'*110, font=('Courier New Baltic',12),fg='violet red',bg='misty rose').place(x=25,y=(height+130))
        tk.Label(nw8, text='YOU PAY : ', font=('Courier New Baltic',15),fg='violet red',bg='misty rose').place(x=50,y=(height+160))
        tk.Label(nw8, text='₹'+str(gst+tot+50), font=('Courier New Baltic',15),fg='violet red',bg='misty rose').place(x=455,y=(height+160))

        tk.Button(nw8, text = "Proceed",bg='violet red',fg='misty rose',width=10,font=('Courier New Baltic',10),command = lambda:[nw8.destroy(),self.payment()]).place(x=300,y=(height+200))
        tk.Button(nw8, text = "Cancel Order",bg='violet red',fg='misty rose',width=10,font=('Courier New Baltic',10),command = r.destroy).place(x=300,y=(height+240))
        tk.Label(nw8, text ="WARNING: All saved changes will be lost if you cancel.",bg='misty rose',fg='red' ).place(x=210,y=(height+280))

    def payment(self):
        global nw9
        nw9 = tk.Toplevel(r); nw9.title("Payment Details")
        nw9.configure(background='misty rose')
        nw9.geometry('600x500')
        self.Uname = tk.StringVar()
        self.phoneno = tk.StringVar()
        self.houseno = tk.StringVar()
        self.area = tk.StringVar()
        self.city = tk.StringVar()
        self.state = tk.StringVar()
        self.pincode = tk.StringVar()
        
        tk.Label(nw9, text ="Name :",font=('Courier New Baltic',12),bg='misty rose',fg='violet red' ).place(x= 20, y= 40)
        tk.Entry(nw9, textvariable=self.Uname, width = 30).place(x= 220, y = 40)

        tk.Label(nw9, text = "Phone no. :",font=('Courier New Baltic',12),bg='misty rose',fg='violet red').place(x= 20, y= 80)
        tk.Entry(nw9, textvariable=self.phoneno, width = 15).place(x= 220, y = 80)

        tk.Label(nw9, text ="Address-",font=('Courier New Baltic',15), bg='misty rose',fg='violet red').place(x=20, y = 120)

        tk.Label(nw9, text ="House no. :",font=('Courier New Baltic',12), bg='misty rose',fg='violet red').place(x=20, y = 160)
        tk.Entry(nw9, textvariable=self.houseno, width = 15).place(x= 220, y=160)

        tk.Label(nw9, text ="Street Name/Area :",font=('Courier New Baltic',12), bg='misty rose',fg='violet red').place(x=20, y = 200)
        tk.Entry(nw9, textvariable=self.area, width = 40).place(x= 220, y=200)

        tk.Label(nw9, text ="City :",font=('Courier New Baltic',12),bg='misty rose',fg='violet red').place(x= 20, y= 240)
        tk.Entry(nw9, textvariable=self.city, width = 15).place(x= 220, y=240)
        tk.Label(nw9, text ="State :",font=('Courier New Baltic',12),bg='misty rose',fg='violet red').place(x= 20, y= 280)
        tk.Entry(nw9, textvariable=self.state, width = 15).place(x= 220, y=280)
        tk.Label(nw9, text ="Pincode :",font=('Courier New Baltic',12),bg='misty rose',fg='violet red').place(x= 20, y= 320)
        tk.Entry(nw9, textvariable=self.pincode, width = 15).place(x= 220, y=320)
        tk.Button(nw9, text ="Cash On Delivery",font=('Courier New Baltic',12),fg='misty rose',bg='violet red',command = self.thankyou).place(x = 200, y = 380, width = 150)
        tk.Label(nw9, text ="Coming Soon : Credit card , UPI , Net Banking and other payment options.",bg='misty rose',fg='red' ).place(x= 100, y= 420)
        
    def thankyou(self):
        global nw10
        nw10 = tk.Toplevel(r); nw10.configure(background='misty rose')
        
        global Uname, phoneno, houseno, area, city, state, pincode
        Uname=self.Uname.get();  phoneno=self.phoneno.get()
        houseno=self.houseno.get(); area=self.area.get()
        city=self.city.get(); state=self.state.get()
        pincode=self.pincode.get()
        if Uname=='' or phoneno=='' or houseno=='' or area=='' or city=='' or state=='' or  pincode=='':
            nw10.title("Pop Up"); nw10.geometry("230x80")
            tk.Label(nw10,text ="WARNING\nField(s) Can't Be Empty!",font=('Courier New Baltic',10),bg='misty rose',fg='red').place(x=40,y=20)
        else:
            nw9.destroy()
            nw10.title("Thankyou"); nw10.geometry("600x400")
            tk.Label(nw10,text ="Your order will be delivered within 3 working hrs",font=('Courier New Baltic',20),bg='misty rose',fg='violet red').place(x=10,y=100)
            tk.Button(nw10,text ="Download bill as PDF",font=('Courier New Baltic',18),fg='misty rose',bg='violet red',command = lambda:[self.result(),self.pdf()]).place(x=170,y=160)
            tk.Label(nw10,text ="Thank you for shopping with us!",font=('Courier New Baltic',20),bg='misty rose',fg='blue').place(x=95,y=230)
            tk.Button(nw10,text ="Exit",font=('Courier New Baltic',13),fg='misty rose',bg='violet red',command = r.destroy).place(x=270,y=300)

    def result(self):
        nw10.destroy()
        nw11 = tk.Toplevel(r); nw11.title("PDF")
        nw11.configure(background='misty rose')
        nw11.geometry('220x180')
        tk.Label(nw11,text ="PDF Downloaded\n  Successfully!!",font=('Courier New Baltic',17),bg='misty rose',fg='violet red').place(x=16,y=35)
        tk.Button(nw11,text ="EXIT",font=('Courier New Baltic',13),fg='misty rose',bg='violet red',command = r.destroy).place(x=80,y=120)

    def pdf(self):
        D=datetime.date.today()
        address = houseno+','+area+','+city+','+state+'-'+pincode

        pdf=FPDF()
        pdf.add_page()
                
        pdf.set_font('helvetica',size=10)
        pdf.cell(0,2,txt='Bill Date : '+str(D.day)+'/'+str(D.month)+'/'+str(D.year),ln=0,align='R')
        pdf.set_font('helvetica',size=16)
                
        pdf.image('logo2.png',1,0,85,70,'PNG')
        pdf.cell(-175,10,txt="CURETRY PHARMACY BILL",ln=1,align="C")
        pdf.cell(100,10,txt="_"*160,ln=1,align="C")
        pdf.cell(200,10,txt="NAME:  "+Uname.title(),ln=1,align="L")
        pdf.cell(200,8,txt="ADDRESS:  "+address,ln=1,align="L")
        pdf.cell(200,10,txt="CONTACT:  "+phoneno,ln=1,align="L")

        pdf.cell(100,10,txt="-"*160,ln=1,align="C")
        a=' '*55+"MEDICINE NAME"+' '*30+"QUANTITY"+' '*30+"PRICE"
        pdf.cell(100,10,txt=a,ln=1,align="C")
        pdf.cell(100,10,txt="-"*160,ln=1,align="C")
        cart = CART[2:]
        for i in cart:
            pdf.cell(93,10,txt=i[0],ln=0)
            pdf.cell(75,10,txt=str(i[1]),ln=0)
            pdf.cell(100,10,txt=str(i[2]),ln=1)
        pdf.cell(100,10,txt="-"*160,ln=1,align="C")
            
        b = "GST(18%):"+" "*89+str(float(gst)) 
        pdf.cell(100,10,txt=b,ln=1)
        c = "Shipping Charges:"+" "*77+"50.0"
        pdf.cell(100,10,txt=c,ln=1)

        pdf.set_text_color(255,0,0) 
        d = "TOTAL AMOUNT:"+" "*72+"Rs. "+str(tot+gst+50)
        pdf.cell(100,10,txt=d,ln=1)
        pdf.output("Curetry Bill.pdf")

        
if __name__ == '__main__':
    GUI().createUI()
