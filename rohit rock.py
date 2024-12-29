import pandas as pd
import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user='root',passward='789',database='carsowroom',charset='utf8')

if mycon.is_connected():
    print('connection is done')
    df=pd.read_sql('select * from inventry',mycon)
    print(df)
else:
    print('connection nahi ho paya')
