#capitalize
print('______CAPITALIZE--------')
a='sky is blue in colour'
resa=a.capitalize()
print(resa)

print('----------------------------------')
a='sky is blue in colour'
resa=a.capitalize()
print(resa)
if resa=="sky is blue in colour":
    print("you are corret")
else:
    print('you are wrong')

print('-------------------------------------')
a='sky is blue in colour'
resa=a.capitalize()
print(resa)
if resa=="Sky is blue in colour":
    print("you are correct")
else:
    print('you are wrong')

print('-------------TITLE----------')


#Title
b='bee for boy'
resb=b.title()
print(resb)

print('----------------------------')
b='bee For boy'
resb=b.title()
print(resb)
if resb =="Bee For Boy":
    print('you are correct')
else:
   print('you are wrong')

print('----------------------------------------')
b = 'bee for boy'
resb = b.title()
print(resb)
if resb == "bee for boy":
       print('you are correct')
else:
       print('you are wrong')

print('-----------UPPER----------------')
#upper
c='cee for Cat'
resc=c.upper()
print(resc)

print('-----------------------------------------')
c='Cee for cat'
resc=c.upper()
print(resc)
if resc =="CEE FOR CAT":
    print('you are correct')
else:
   print('you are wrong')

print('---------------------------------------')
c='Cee for cat'
resc=c.upper()
print(resc)
if resc =="Cee For Cat":
    print('you are correct')
else:
   print('you are wrong')

#Lower case
print('----LOWER CASE------------')
d='DEE FOR DOG'
resd=d.lower()
print(resd)

print('-----------------------------')
d='DEE FOR DOG'
resd=d.lower()
print(resd)
if resd=="DEE FOR DOG":
    print('you are correct')
else:
    print('you are wrong')

print("--------------------------------")
d='DEE FOR DOG'
resd=d.lower()
print(resd)
if resd=="dee for dog":
    print('you are correct')
else:
    print('you are wrong')

#SWAP CASE
print('======SWAP CASE=========')
e="EEE FOR ELEPHANT"
rese=e.swapcase()
print(rese)

print('---------------------------')
e="eee for elephant"
rese=e.swapcase()
print(rese)

print('------------------------------------')
e="EEE FOR ELEPHANT"
rese=e.swapcase()
print(rese)
if rese=='eee for elephant':
    print("you are correct")
else:
    print("you are wrong")
print('-----------------------------------------')

#Startswith
se="Sky is in Blue Colour"
ans=se.startswith('s')
print(ans)
print("---------------------------")
sd="Sky Is In Blue Colour "
Ans=sd.startswith('S')
print(Ans)
print('-----------END WITH-------------')

#endswith
f='Sun Rises In The Morning'
sol=f.endswith('G')
print(sol)
print('-------------------------------------')
f1="sun rises in the morning"
sol1=f1.endswith('g')
print(sol1)

#is lower
print('---------------IS LOWER---------------')
G="hello world"
G1=G.islower()
print(G1)

print('----------------------------------')

G1="HELLO WORLD"
SOLG2=G1.islower()
print(SOLG2)


#IS UPPER
print('------------------IS UPPER------------')
g="WELCOME TO PYTHON"
G2=g.isupper()
print(G2)

print('----------------------------------')
h='welcome to python'
h2=h.isupper()
print(h2)

print('------------- IS TITLE-----------------')
i='The Globe Is Round'
i2=i.istitle()
print(i2)

print('____________________________')
i1='the globe is round'
i23=i1.istitle()
print(i23)

print('----------IS ALPHA------------')
alp='aplha'
resalp=alp.isalpha()
print(resalp)

print('__________________')
alp1='234534'
resalp1=alp1.isalpha()
print(resalp1)

print('-----------Is Digit-------')
dig='234534'
redig=dig.isdigit()
print(redig)

print('-----------------------------')

dig1='is it digit'
redig2=dig1.isdigit()
print(redig2)