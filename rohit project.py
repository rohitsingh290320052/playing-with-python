import mysql.connector as sql
import sys

#connect to mysql database
db=sql.connect(host="localhost",user="root",passwd="789",database="mysql")
cursor=db.cursor()
#check database is connected
if db.is_connected():
    print("Database connected")

#MENU FOR STUDENT MARKS MANAGEMENT SYSTEM SOFTWARE
print("*************************************************")
print("WELCOME TO MY PROJECT STUDENT MARKS MANAGEMENT SYSTEM")
print("*************************************************")
print()
while(1):
    print("1:TO CREATE TABLE FOR THE FIRST TIME")
    print("2:TO DISPLAY TABLES OF DATABASE")
    print("3:TO SHOW FIELDS OF TABLE")
    print("4:TO DISPLAY ALL DATA")
    print("5:TO ADD NEW STUDENT")
    print("6:TO SEARCH A STUDENT RECORD")
    print("7:TO CHANGE MARKS OF STUDENT")
    print("8:TO DELETE STUDENT ")
    print("9:EXIT")
    print()
    ch=int(input("ENTER YOUR CHOICE"))
#Creating table for the first time
    if ch==1:
        try:
            print(" Creating STUDENT table")
            sql = "CREATE TABLE student(ROLL int(4) PRIMARY KEY,name varchar(15) NOT NULL,class char(3) NOT NULL,sec char(1),mark1 int(4),mark2 int(4),mark3 int(4),mark4 int(4),mark5 int(4),total int(4),per float(4));"
            cursor.execute(sql)
            mycon.commit()
        except:
            print("sorry some error occured")
#Displaying tables of database 
    if ch==2:
        try:
            cursor.execute("show tables")
            for i in cursor:
                print(i)
        except:
            print("sorry some error occured")
#Displaying Tables fields
    if ch==3:
        try:
            table=input("enter table name")
            cursor.execute("desc %s"%table)
            for i in cursor:
                print(i)
        except:
            print("sorry some error occured")
#Displaying all records of table
    if ch==4:
        try:
            cursor.execute("select * from student")
            data=cursor.fetchall()
            print("ROLL NO","STUDENT NAME","CLASS","SECTION","SUBJECT1","SUBJECT2","SUBJECT3","SUBJECT4","SUBJECT5","TOTALMARKS","PERCENTAGE")
            for i in data:
                j=str(i).split()
                for k in j:
                    print(k,end="     ")
                print()
        except:
            print("SORRY SOME ERROR OCCURED")
#inserting new record into table
    if ch==5:
        r=int(input("Enter student roll number"))
        name=input("ENTER STUDENT NAME")
        c=input("ENTER CLASS OF STUDENT")
        s=input("ENTER SECTION OF STUDENT")
        m1=int(input("ENTER MARKS IN SUBJECT1"))
        m2=int(input("ENTER MARKS IN SUBJECT2"))
        m3=int(input("ENTER MARKS IN SUBJECT3"))
        m4=int(input("ENTER MARKS IN SUBJECT4"))
        m5=int(input("ENTER MARKS IN SUBJECT5"))
        t=m1+m2+m3+m4+m5
        per=t/5
        query="insert into student values(%d,'%s','%s','%s',%d,%d,%d,%d,%d,%d,%d)"%(r,name,c,s,m1,m2,m3,m4,m5,t,per)
        cursor.execute(query)
        print("STUDENT RECORD SAVED IN TABLE")
        db.commit()
#searching student details
    if ch==6:
        print("1:TO SERACH BY STUDENT ROLL NUMBER")
        print("2:TO SEARCH BY STUDENT NAME")
        c=int(input("ENTER YOUR CHOICE"))
        #searching by student roll number
        if c==1:
            try:
                roll=int(input("ENTER STUDENT ROLL NUMBER TO SEARCH"))
                qry="select * from student where roll=%d"%roll
                cursor.execute(qry)
                data=cursor.fetchall()
                if len(data)==0:
                    print("STUDENT NOT FOUND")
                print("ROLL NO","STUDENT NAME","CLASS","SECTION","SUBJECT1","SUBJECT2","SUBJECT3","SUBJECT4","SUBJECT5","TOTALMARKS","PERCENTAGE")
                for i in data:
                    j=str(i).split()
                    for k in j:
                        print(k,end="    ")
                    print()
            except:
                print("SORRY SOME ERROR OCCURED")
                
        #searching by student name
        if c==2:
            try:
                name=input("ENTER STUDENT NAME TO SEARCH")
                qry="select * from student where name='%s'"%name
                cursor.execute(qry)
                data=cursor.fetchall()
                if len(data)==0:
                    print("STUDENT NOT FOUND")
                print("ROLL NO","STUDENT NAME","CLASS","SECTION","SUBJECT1","SUBJECT2","SUBJECT3","SUBJECT4","SUBJECT5","TOTALMARKS","PERCENTAGE")
                for i in data:
                    j=str(i).split()
                    for k in j:
                        print(k,end="    ")
                    print()
            except:
                print("SORRY SOME ERROR OCCURED")
            
            
#TO update student marks
    if ch==7:
        try:
            roll=int(input("ENTER ROLL NUMBER OF STUDENT WHOSE MARKS TO BE UPDATE"))
            qry="select * from student where roll=%d"%roll
            cursor.execute(qry)
            data=cursor.fetchall()
            if len(data)==0:
                print("STUDENT NOT FOUND")
            else:
                m1=int(input("ENTER UPDATED MARKS IN SUBJECT1"))
                m2=int(input("ENTER UPDATED MARKS IN SUBJECT2"))
                m3=int(input("ENTER UPDATED MARKS IN SUBJECT3"))
                m4=int(input("ENTER UPDATED MARKS IN SUBJECT4"))
                m5=int(input("ENTER UPDATED MARKS IN SUBJECT5"))                
                t=m1+m2+m3+m4+m5
                per=t/5
                qry="update STUDENT SET mark1=%d,mark2=%d,mark3=%d,mark4=%d,mark5=%d,total=%d,per=%d where roll=%d"%(m1,m2,m3,m4,m5,t,per,roll)
                cursor.execute(qry)
                print("STUDENT RECORD UPDATED")
                db.commit()
        except:
            print("SORRY SOME ERROR OCCURED")
        
# Delete student record from table
    if ch==8:
        try:
            roll=int(input("ENTER STUDENT ROLL NUMBER ,YOU WANT TO DELETE"))
            qry="select * from student where roll=%d"%roll
            cursor.execute(qry)
            data=cursor.fetchall()
            if len(data)==0:
                print("STUDENT NOT FOUND IN TABLE")
            else:
                qry="delete from student where roll=%d"%(roll)
            cursor.execute(qry)
            print("STUDENT RECORD DELETED FROM TABLE")
            db.commit()
        except:
            print("SORRY SOME ERROR OCCURED")
            #Exit from program
    if ch==9:
        sys.exit()


db.close()

