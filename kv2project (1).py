from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    ID= S_ID.get()
    Name= S_Name.get()
    Fname= S_Fname.get()
    Mname= S_Mname.get()
    if(ID=="" or Name=="" or Fname=="" or Mname=="" ):
        MessageBox.showinfo("Insert Status","All Fields are required")
    else:
        con=mysql.connect(host="localhost", user="root", passwd="Dev@1987", database="class12")
        cursor=con.cursor()
        cursor.execute("insert into sdetail values('"+ Admno +"','"+ Name +"','"+ Fname +"','"+ Mname +"')")
        cursor.execute("commit");
        MessageBox.showinfo("Insert Status","Insert Successfully");
        show()
        S_ID.delete(0, 'end')
        S_Name.delete(0, 'end')
        S_Fname.delete(0, 'end')
        S_Mname.delete(0, 'end')
        con.close();

def delete():
    if(S_ID.get()==""):
        MessageBox.showinfo("Delete Status", "ID is compulsory for delete")
    else:
        con=mysql.connect(host="localhost", user="root", passwd="Dev@1987", database="class12")
        cursor=con.cursor()
        cursor.execute("delete from sdetail where Admno=' "+S_Admno.get()+"'")
        cursor.execute("commit");
        S_ID.delete(0, 'end')
        S_Name.delete(0, 'end')
        S_Fname.delete(0, 'end')
        S_Mname.delete(0, 'end')
        MessageBox.showinfo("Delete Status","Deleted Successfully");
        con.close();

def update():
    ID= S_ID.get()
    Name= S_Name.get()
    Fname= S_Fname.get()
    Mname= S_Mname.get()

    if(ID==" " or Name==" " or Fname==" " or Mname==" " ):
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con=mysql.connect(host="localhost", user="root", passwd="Dev@1987", database="class12")
        cursor=con.cursor()
        cursor.execute("update sdetail set ID=' "+ID+"',Name=' "+Name+"',Fname=' "+Fname+"',Mname=' "+Mname+"' where ID='"+ID+"'")
        cursor.execute("commit");
        show()
        S_ID.delete(0, 'end')
        S_Name.delete(0, 'end')
        S_Fname.delete(0, 'end')
        S_Mname.delete(0, 'end')
        MessageBox.showinfo("Update Status","Updated Successfully");
        con.close();

def get():
    if(S_ID.get()==""):
        MessageBox.showinfo("Fetch Status", "Admno is compulsory for display")
    else:
        con=mysql.connect(host="localhost", user="root", passwd="Dev@1987", database="class12")
        cursor=con.cursor()
        cursor.execute("select * from sdetail where Admno=' "+S_Admno.get()+" ' ")
        rows=cursor.fetchall()
        S_Name.delete(0, 'end')
        S_Fname.delete(0, 'end')
        S_Mname.delete(0, 'end')
        for row in rows:
            S_Name.insert(0, row[1])
            S_Fname.insert(0, row[2])
            S_Mname.insert(0, row[3])
        con.close();

def show():
    con=mysql.connect(host="localhost", user="root", passwd="Dev@1987", database="class12")
    cursor=con.cursor()
    cursor.execute("select * from sdetail")
    rows=cursor.fetchall()
    for row in rows:
        insertData=str(row[0])+'        '+row[1]+'    '+row[2]+'   '+row[3]
        list.insert(list.size()+1, insertData)
    con.close()
    
# for Main Window.......
root=Tk()
root.title("Kv2 Project")
root.geometry("1000x600")

L1=Label(root, text="Kendriya Vidyalaya No.2, Agra", font=("Rockwell",40), fg="Blue").pack()

L2=Label(root, text="VACCINATION", font=("Rockwell",30), fg="Red").pack()

#for Labels.....
ID=Label(root, text="ID",font=("Ariel",20), fg="Black").place(x=100,y=200)
Name=Label(root, text="Name of Student",font=("Ariel",20), fg="Black").place(x=100,y=240)
Fname=Label(root, text="Father Name",font=("Ariel",20), fg="Black").place(x=100,y=280)
Mname=Label(root, text="Mother Name",font=("Ariel",20), fg="Black").place(x=100,y=320)

#for Text Boxes.....
S_ID=Entry(root,font=("Ariel",10))
S_ID.place(x=400,y=200,width=350,height=25)
S_Name=Entry(font=("Ariel",10))
S_Name.place(x=400,y=240,width=350,height=25)
S_Fname=Entry(font=("Ariel",10))
S_Fname.place(x=400,y=280,width=350,height=25)
S_Mname=Entry(font=("Ariel",10))
S_Mname.place(x=400,y=320,width=350,height=25)
#for Buttons......
Insert=Button(root, text="Insert",font=("Rockwell",15), fg="White",bg="#d77337", command=insert).place(x=200,y=500)
Delete=Button(root, text="Delete",font=("Rockwell",15), fg="White",bg="#d77337", command=delete).place(x=300,y=500)
Update=Button(root, text="Update",font=("Rockwell",15), fg="White",bg="#d77337",command=update).place(x=400,y=500)
Get=Button(root, text="Get",font=("Rockwell",15), fg="White",bg="#d77337",command=get).place(x=500,y=500)
#for Display the contents in List Box.....
list= Listbox(root)
list.place(x=790,y=200,height=150, width=400)
show()
root.mainloop()
