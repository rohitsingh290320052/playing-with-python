import pandas as pd
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root", passwd="789",database="cars",charset="utf8")
if mycon.is_connected():
    print("connection is done")
    df=pd.read_sql("select * from rrr",mycon)
    print(df)
else:
    print("nahi ho paya")
