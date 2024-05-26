#Question 1/A :

d={}
L1=['HTTP','HTTPS','FTP','DNS']
L2=[80,443,20,53]
for i , j in zip (L1,L2):
    d[i]=j
print(d)


#-------------------------------------------------------
#Question 1/B :

def factorial(k):
    if k == 0 or k == 1:
        return 1
    else:
        t= k * factorial(k - 1)
        return t
number = int(input("Enter integer: "))
if number > 0:
    result = factorial(number)
    print("factorial of: ", number, "is: ", result)
else:
    print("Error")


#---------------------------------------------------------
#Question 1/C :

L=['Network','Bio','Programming','Physics','Music']
i = 0
for i in range(len(L)):
    if L[i].startswith('M'):
        print(L[i])


#----------------------------------------------------------
#Question 1/D :

k={h:h+1 for h in range(11)}
print(k)



