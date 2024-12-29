saloni=input("koi message type kar dijiye:")
kshma={}

for i in saloni:
    if i in kshma:
        kshma[i]=kshma[i]+1
    else:
        kshma[i]=1

for a,b in kshma.items():
    print(a,":",kshma[a],end=",")
    
    
    
