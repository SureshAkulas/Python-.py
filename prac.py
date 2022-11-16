'''s1="apple is a fruit\
      apple is red in color\
      apple is healthy\
      apple keeps doctor away\
      apple grows in cold area"
res=s1.replace("apple","mango",4)
print(res)
res1=res.replace("mango","grapes",1)
print(res1)
res2=res1.replace("mango","orange",1)
print(res2)
res3=res2.replace('mango','banana',1)
print(res3)
#find
a='Blue''Blue''Blue''Blue''Blue''Blue'
ra=a.find('Blue')
print(ra)
b=a.rfind("Blue")
print(b)
c=a.find('Blue',ra+1)
print(c)
d=a.find("Blue",c+1)
print(d)
#Index
a='sky is blue in color'#doubt
ra=a.index('sky')
print(ra)
r1=a.rindex('sky')
print(r1)
#r2=a.index('blue')
#print(r2)

#COUNT
c="sky is blue in color"
print(len(c))
r=c.center(30,'-')
print(r)
print(len(r))

s="Hello World" #how we can add more space.. it showing over all space..
r=s.rjust(20,'-')
print(r)
print(len(r))

#converting str to int by input
num=input('Enter your Number:')
print(type(num))
print(num)
cnum=int(num)
print(type(cnum))
print(cnum)

n=int(input('n:'))
print(n)
print(type(n))

#count 
a="he is laughing as hahahaha"
print(a)
res=a.count('h')
print(res)
#strip
a="       india is my country      "
print(a)
print(len(a))
res=a.lstrip()
print(res)
print(len(res))

#JOIN
b="world"
res="".join(b)
print(res)
k=['Apple','Mango','Banana','Carrot','Dates','Kiwi']
print(len(k))
r=" ".join(k)
print(r)
print(len(r))

l2=['100','200','300','400','500']
print(l2)
print(len(l2))
res1='***'.join(l2)
print(res1)
print(len(res1))
print(l2[0])'''

#split
'''d="hyd -ts**bhopal-mp**chennai-tn**vizag-ap"
print(d)
print(type(d))
res=d.split("**")
print(res)
print(res[-3])'''

'''c='sky is blue blue is the blue color blue sky'

res1=c.replace ('blue','Blue',2)
res2=res1.replace('Blue','blue',1)
print(res2)
res3=res2.split('Blue')
print(res3)'''

#print("Good Morning")
"""a="Good"
b="Morning"
print(a,b)
print(a+b)
print(a,b,sep=" ")
print(a,b,sep="")
print(a,b,sep="\t")
print(a,b,sep=" *** ")"""

'''print("INDIA",end=" ")
print("USA",end=" ** ")
print("FRANCE","--")
print("JAPAN")
print('--------------')
print("INDIA",end="\n")'''

print("-----------------------")

#format
'''n="naren"
a="Hyderabad"
l=5
print("Name:{}".format(n))

print("Name:{}""City:{}""age:{}".format(n,a,l))

s="Name:{}""City:{}""age:{}"
print(s.format(n,a,l))'''

'''print("----------------------------")
a=450
b=450
c=40
d=(c<a)
print(d)
print("---------------")
s="HYDERABAD"  #Why some times tru and false...?
r="BANGALORE"
print(s==r)

print("--------------------------")
b1=int(input("Enter Number:"))
b2=int(input("Enter Number:"))
b3=int(input("Enter Number:"))'''

'''if b1>=b2 and b2>=b3:
    print(b1)
elif b2>=b3:
    print(b2)
else:
    print(b3)'''

'''res=(b1 if(b1 >= b2 and b1 >= b3) else (b2 if b2 >= b3 else b3))
print(res)'''

'''x=1
while(x<=10):
    if x%2 != 0:
        print(x)
    x=x+1
print('-------------------')
x=1
while(x<=10):
    if x%2 == 0:
        print(x)
    x=x+1
print("-------------------")
x=1
while(x<=5):
    print(x)
    x=x+1
print('--------------------')
a=int(input("Number:"))
b=int(input("Divisor:"))

x=1
while (x<=a):
    if x%b == 0:
        print(x)
    x=x+1
print('-----------------------')
num=int(input("number:"))
d=int(input('divisor:'))
x=1
while x <= num:
    if x%d ==0:
        print(x)
    x+=1
print("----------------------")
x=1 
while x<=5:
    print("INDIA")
    x+=1'''
'''print('--------------------------')
x=10  #descending
while x>=1:
    print(x)
    x-=1
print('--------------------------------')
x=10
while x>=1:
    print(x)
    x-=1

x=10
while x>=1:
    print(x)
    x-=1
x=1
while x<=10:
    print(x)
    x+=1
print('--------------------------------')
x=1 #Ascending
while x<=5:
    print(x)
    x+=1
print("----------------------------------")
num=int(input("number:"))
d=int(input("Divisor:"))
x=1
while x<=num:
    if x%d ==0:
        print(x)
    x+=1'''
'''x=1 # Ascending order
while x<=10:
    print(x)
    x+=1

i=10 # Descending order.
while i>=1:
    print(i)
    i-=1'''

x=1
while x<=5:
    print("welcome to india")
    x+=1






