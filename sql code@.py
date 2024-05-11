import mysql.connector
sqlobj=mysql.connector.connect(host="localhost", user="root", password="usrs123$")             
cur=sqlobj.cursor()

cur.execute('create database curetry_new')
cur.execute('use curetry_new')

#CUSTOMER DETAILS
cur.execute('''create table customer_details(First_Name char(70), Last_Name char(70),
                Email char(60) primary key, Password char(60))''')
cur.execute('''insert into customer_details values("Swathi","Uday","swathiuday21@gmail.com","usrs123$"),
               ("a","b","c","d"),("Ashvita","Ramanan","ashu612@gmail.com","iitbhu22"),
               ("Asmita","Kumaravel","asmita162@yahoo.co.in",'btsforlife'),("Vaishnavi","A S","vaishu2005@gmail.com","cutie"),
               ("Saritha","R","saritha194@yahoo.co.in",'DSKTrDp'),("Sudhiksha","G","sudhi2411@gmail.com",'crazy$kit'),
               ("Praveena","S","praveena@gmail.com",'Pra*Hesh'),("Damin","Rido","daminRido@gmail.com","ProFencing")''')


#ADMIN USERID & PASSWORD
cur.execute('create table if not exists admin(Username char(60), Password char(60))')
cur.execute('insert into admin values("admin@curetry139","DrJvRv2112"),("u","p")')


#For MEDICINES
cur.execute('''create table if not exists med(ID char(10), Name char(70),
               Type char(60), Quantity int, Price float(8,2))''')

cur.execute('''insert into med values("M001","Benedryl-Dry","Syrup",18,130.00),
               ("M005","Concor","Tab",6,20.00),("M011","Paracetamol","Tab",45,17.5),
               ("M012","Dolo-650","Tab",30,15.00),("M030","Zincovit","Tab",55,10.00),
               ("M044","Fluticone","Nasal Spray",5,297.45),("M051","Crocin","Syrup",13,100.99),
               ("M063","Montek 10mg","Tab",20,23.00),("M064","Montek 20mg","Tab",20,38.00),
               ("M078","Levolin","Inhaler",8,225),("M100","Uniclave 650mg","Tab",10,16.75)''')

cur.execute('''insert into med values("M019","Azythromycin","Tab",24,17.5),
               ("M008","Amoxyclav","Tab",13,15.75),("M023","Okacet","Tab",40,11),
               ("M041","Dexorange","Syrup",5,160.00),("M055","Mihron","Tab",33,9.5)''')

#cur.execute("alter table med drop ID")
sqlobj.commit()

            


            

    
