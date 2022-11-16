# if else

'''input("Enter student name:")
int(input("Class:"))
m=int(input("English Marks:"))
m1=int(input('Science Marks:'))
m2=int(input("computer marks:"))
m3=int(input("Social Marks:"))
Total=m+m1+m2+m3
print(Total)
Average=Total/4
print(Average)
if (Average>=40):
    print("Congrats You are passed")
else:
    print("Sorry you failed")

print('------------------------------------')

e=input("Enter your Employee Name:")
e1=int(input("Enter your Employee Experience:"))
e2=input("Enter your Employee Technology:")
e3=int(input('Employee Salary:'))
if (e1>=8):
    print("Senior Resource")
else:
    print("Junior Resource")

print('----------------------------------------')

input("Enter Car Model:") #what if car model has both no. and alpha
c=input("Enter Car Colour:")
c2=int(input("Enter Car Price:"))
if c == "Blue":
    print('Extra 20000:')
    print('Car Price:',c2)
    print('Total Final price:',20000+c2)
elif c== "Red":
    print( 'Extra 25000:')
    print('Car Price:',c2)
    print('Total Final Price:',25000+c2)
elif c=='Yellow':
    print('Extra 30000:')
    print('Car Price:',c2)
    print('Total Final Price:',30000+c2)
else:
    print('Extra Charges:0.00')
    print("Total Final Price:",c2)

print('--------------------------------------------------')'''

input('Employee Name:')
a=input('Employee Designation:')
b=int(input('Employee Salary:'))
a=a.title()
if a == "Project Manager":
    c=b/100*22 # Hiked Percentage
    print('Hiked Amount:',c)
    print('revised salary:',c+b)
elif a == "Technical Manager":
    c  =   b/100*20  # hike percent
    print('Hiked Amount:',c)
    print("revised amount:",c+b)
elif a=="Developer":
    c=Hike_percent=b/100*16
    print('Hiked Amount:',c)
    print('revised amount:',c+b)
elif a=="Tester":
    c=hike_percent=b/100*14
    print("Hiked Amount:",c)
    print('revised amount:',c+b)
else:
    c=Hike_percent=b/100*12
    print("Hiked Amount:",c)
    print('revised Amount:',c+b)

print('--------------------------------------')
