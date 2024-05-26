#Question 2 :

dec= 0
m=[]
n=input("enter binary number : ")
for i in n:
    m.append(i)
m.reverse()
try:
    for i in range(len(m)):
        dec+=int(m[i]) * 2**i
    print(dec)
except:
    print("error")