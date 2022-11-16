#Key words
# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not
import keyword
#inbuilt function is inside library known predefined.
#user defined function is known non inbuilt function.
#def suresh():
a=200
b=300
c=a+b
print(c)
#variable define value
#value printed as same.
klist=list(keyword.kwlist)  #Doubt here...& where we use ASCII in real time and it uses.& def functions how and were
print(klist)
c=0
for i in klist:
    print(i)
    c=c+1
    print(c)

#identifiers.
def sky():
    x=2
    y=4
    z=6
    res=x+y+z
    print(res)
sky()
class arjunclass:
    def sky1(): #sky is inbuilt user defined function.
        x = 2 #identifer can be a classname,function,name,classnobjectname
        y = 4
        z = 6
        res = x + y + z
        print(res)
#function inside the class is called as method.
sky()
#identifier with alphabets.
a=100
print(a)
B=200
print(B)
c='east'
print(c)
f34=500
print(f34)
#123="apple" #can not assign value to another value called as literal
print(123)
apple="banana"
print(apple)
