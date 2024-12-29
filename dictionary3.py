x=input("enter any number")
temp={0:'zero',1:'one',2:'two',3:'three'}

for ch in x:
    pqr=int(ch)
    xyz=temp[pqr]
    result=result+" "+ xyz

print(result)
