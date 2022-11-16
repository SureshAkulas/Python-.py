'''input("Enter Car Model:")
c=input("Enter Car Colour:")
c2=int(input("Enter Car Price:"))
c=c.title()
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
print('______________________________________________')'''
'''input("Enter Car Model:")
c=input("Enter Car Color:")  #Here i'm unable to use elif....
c2=int(input("Enter Car Price:"))
c=c.title()
res = ("Extra:20000"), ("Car Price:",c2), ("Total Price:",20000+c2) if c == "Blue" else ("Extra 25000:"),\
      ("Car Price:",c2), ("Total Price:" , 25000+c2) if c == 'Red' else ("Extra: 30000"), ("Car Price:",c2), \
      ("Total Price:",30000+c2) if c == "Yellow" else ("Extra Charges:0.00"),("Total Price:",c2)
print(res)'''
'''print("---------------------------------------------------")
e=input("Enter your Employee Name:")
e1=int(input("Enter your Employee Experience:"))
e2=input("Enter your Employee Technology:")
e3=int(input('Employee Salary:'))
if (e1>=8):
    print("Senior Resource")
else:
    print("Junior Resource")
print('-------------------------------------------------------')
res=("senior resource") if (e1>=8) else ("Junior Resource")
print(res)'''

print("----------------------------------------------")

input("Enter student name:")
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
res=("Grade A") if (Average >= 80 and Average < 70) else ('Grade B') if (Average >= 70 and Average <80) \
      else ("Grade C") if (Average >=55 and Average  <70) else ("Fail")
print(res)


print('--------------------------------')
res1=("congrats you are passed") if (Average >=40) else ("Sorry you failed")
print(res1)
print("-----------------------------------------")

Age=int(input('Enter age:'))
res=("You are Eligible") if (Age >= 18) else ("Not Eligible:")
print(res)