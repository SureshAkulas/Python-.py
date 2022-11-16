
'''x=1 #Ascedning order
while x<=10:
    print(x)
    x+=1

x=10 #Descending order
while x>=1:
    print(x)
    x-=1

num=int(input('Enter Number:')) #Ascending
x=1
while x<=num:
    print(x)
    x+=1

num=int(input("Enter Number:")) # Descending
x=num
while x>=1:
    print(x)
    x-=1


num=int(input("Number:")) #no. of times word should be printed...
N=input("Word:")
x=1
while x<=num:
    print(N)
    x+=1'''

'''x=1  #Even
while x <=10:
    if x%2==0:
        print(x)
    x+=1

num=int(input("Number:")) #Even
x=1
while x<=num:
    if x%2==0:
        print(x)
    x+=1

x=1 #odd
while x<=10:
    if x%2!=0:
        print(x)
    x+=1

num=int(input("Number:")) #odd
x=1
while x<=num:
    if x % 2 !=0:
        print(x)
    x+=1'''

#Division
'''num=int(input('num:'))
d=int(input("Div:"))
x=1
while x<=num:
    if x%d ==0:
        print(x)
    x+=1'''

#Decrementation:

'''import time
x=10
while x>=1:
    print(x)
    x-=1
    time.sleep(0.5)

num=int(input("Number:"))
x=num
while x >=1:
    print(x)
    x-=1
    time.sleep(0.5)

#Incrementation...
x=1
while x<=10:
    print(x)
    x+=1
    time.sleep(0.5)

num=int(input("Number:"))
x=1
while x<=num:
    print(x)
    x+=1
    time.sleep(0.5)'''

#Count:
'''num=int(input("Number:"))
d=int(input("Divisor:"))
x=1
c=0
while x<=num:
    if x % d == 0:
        print(x)
        c=c+1
    x+=1
print("No. of values:",c)'''

#SUm:
'''num=int(input("number:"))
d=int(input("div:"))
x=1
c=0
s=0
while x<=num:
    if x % d == 0:
        print(x)
        c=c+1
        s=s+x
    x=x+1
print(c)
print(s)'''

     #Tables:
'''num=int(input("Table;"))
N=int(input("No.of:"))
x=1
while x<=N:
    print(num,"*",x,"==",(5*x))
    x+=1'''

#Product:
'''num=int(input("Number:"))
d=int(input("Div:"))

x=1
c=0
s=0
p=1
while x<=10:
    if x %d ==0:
        print(x)
        c=c+1
        s=s+x
        p=p*x
    x+=1
print(c,s,p)'''

'''num=int(input("Number"))
for i in range(1,num+1):
    print(i*i)
time.sleep(1)'''

'''x=1 # nested While ascending order.
while x <=3:
    i=1
    while i<=5:
        print(i)
        i+=1
    x=x+1'''

'''x=1 #nested while descending order
while x <=3:
    i=10
    while i>=1:
        print(i)
        i-=1
    x+=1'''
'''x=3
while x <=10:
    i=1
    c=0
    while i <=x:
        if x%i==0:
            c+=1
        i=i+1
        if c==2:
            print(x,"PN")
        x+=1'''

#num=int(input("number:"))  #Nested While PN;
'''x=1
c=0
while x<=num:
    if num%x == 0:
        c+=1
    x+=1
if c==2:
    print(num,"pn")
else:
    print('NPN')

print('--------------------------------')'''
'''x=2 # table i  nested
while x<=num:
    i=1
    while i<=10:
        print(x,"*",i,"==",x*i)
        i+=1
    x+=1'''

'''i=1 #table..
while i<=10:
    print(num,"*",i,"==",num*i)
    i+=1'''
'''while i<=num:
    name=input("Name:")
    cls=input("Class:")
    eng=int(input("English:"))
    sci=int(input("Scinece:"))
    comp=int(input("Computer:"))
    tot=eng+sci+comp
    avg=tot/3
    res="A" if avg >=80 else "B" if avg >=65 and avg <80 else "c"
    print(res)

    ch=input("continue(yes/no)")
    ch=ch.upper()
    if ch !="YES":
        print("thanks")
        break'''
'''i=1
while i<=num:
    name=input("Name:")
    cls=input("Class:")
    eng=int(input("English:"))
    sci=int(input("Scinece:"))
    comp=int(input("Computer:"))
    tot=eng+sci+comp
    avg=tot/3
    res="A" if avg >=80 else "B" if avg >=65 and avg <80 else "c"
    print(res)
    i+=1'''

'''for i in "INDIA":
    print(i)
s="welcome"
for x in s:
    print(x)

list1=["Apple","red","Mango","Green"] #nested
for a in list1:
    print(a)
    for j in list1:
        print(j)

s="india"
for d in s:
    print(d)

a=iter(list1) # to print one after one use ITER
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))'''
'''x=1  # Doubt ?
for x < = 5:
    print(x)
    x+=1
i=1
while i <=5:
    print(i)
    i+=1'''
'''for x in range (1,11,1):
    if x%2==0:
     print(x)
for x in range(1,num,1):
    if x%2==0:
        print(x)
for x in range (1,num+1,1):
    if x%2!=0:
        print(x)'''

'''i=1
while i <=10:
    print(i)
    i+=1'''
'''r=list(range(1,10,1))
print(r)'''
list=["Apple","Banana","Mango","Orange"]
for i in list:
    print(i)