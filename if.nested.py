#nested if
'''input("Student Name:")
int(input("Class:"))
m1=int(input("English:")) #M1= english marks
m2=int(input("Science:")) #m2=science marks
m3=int(input("Computer:")) # m3 = Computer marks
m4=int(input("Attendence:")) #m4=Attendence
m5=Total=m1+m2+m3            # m5=Total marks
print('Total:',m5)
m6=Average=Total/3     # m6 = Average.
print('Average:',m6)
if m6 >= 95:
    m=m6/100*5 # Added attendence # m= extra average
    print("Added Attendence:",m)
    print("Total Average:",m+m6)
    M=m+m6 # variable for over all average:
    if M >= 95:
        print("Grade:A+")
    elif M>=90 <95:
        print("Grade:A")
    elif M>=85 <90:
        print("Grade:B+")
    elif M>=70 < 85:
        print("Grade:B")
    elif M>=50<70:
        print("Grade:C")
    else:
        print("FAILED")
elif m6 >= 85 < 95:
    m = m6/100* 4
    print("Added Attendence:",m)
    print("Total Average:",m+m6)
    M=m+m6
    if M >= 95:
        print("Grade:A+")
    elif M>=90 <95:
        print("Grade:A")
    elif M>=85 <90:
        print("Grade:B+")
    elif M>=70 < 85:
        print("Grade:B")
    elif M>=50<70:
        print("Grade:C")
    else:
        print("FAILED")
elif m6 >= 75 < 85:
    m=m6/100*3
    print("added Attendence:",m)
    print("Total Average:",m+m6)
    M=m+m6
    if M >= 95:
        print("Grade:A+")
    elif M>=90 <95:
        print("Grade:A")
    elif M>=85 <90:
        print("Grade:B+")
    elif M>=70 < 85:
        print("Grade:B")
    elif M>=50<70:
        print("Grade:C")
    else:
        print("FAILED")
elif m6 >= 70<75:
    m=m6/100*2
    print("added Attendence:",m)
    print("Total Average:",m+m6)
    M=m+m6
    if M >= 95:
        print("Grade:A+")
    elif M>=90 <95:
        print("Grade:A")
    elif M>=85 <90:
        print("Grade:B+")
    elif M>=70 < 85:
        print("Grade:B")
    elif M>=50<70:
        print("Grade:C")
    else:
        print("FAILED")
elif m6 >= 65 <70:
    m=m6/100*1
    print("Added Attendence:",m)
    print("Total Average:",m+m6)
    M = m+m6 # added veriable for over all...
    if M >= 95:
        print("Grade:A+")
    elif M>=90 <95:
        print("Grade:A")
    elif M>=85 <90:
        print("Grade:B+")
    elif M>=70 < 85:
        print("Grade:B")
    elif M>=50<70:
        print("Grade:C")
    else:
        print("FAILED")
else:
    print("No Extra Attendence added:0.00")
    print("Total Average:",m6)
    M=m6
    if M >= 95:
        print("Grade:A+")
    elif M>=90 <95:
        print("Grade:A")
    elif M>=85 <90:
        print("Grade:B+")
    elif M>=70 < 85:
        print("Grade:B")
    elif M>=50<70:
        print("Grade:C")
    else:
        print("FAILED")


print('___i did in two ways...__')

input("Student Name:")
int(input("Class:"))
m1=int(input("English:")) #M1= english marks
m2=int(input("Science:")) #m2=science marks
m3=int(input("Computer:")) # m3 = Computer marks
m4=int(input("Attendence:")) #m4=Attendence
m5=Total=m1+m2+m3            # m5=Total marks
print('Total:',m5)
m6=Average=Total/3     # m6 = Average.
print('Average:',m6)
if m6 >= 95:
    m=m6/100*5 # Added attendence # m= extra average
    print("Added Attendence:",m)
    print("Total Average:",m+m6)
    M=m+m6
elif m6 >= 85 < 95:
    m = m6/100* 4
    print("Added Attendence:",m)
    print("Total Average:",m+m6)
elif m6 >= 75 < 85:
    m=m6/100*3
    print("added Attendence:",m)
    print("Total Average:",m+m6)
elif m6 >= 70<75:
    m=m6/100*2
    print("added Attendence:",m)
    print("Total Average:",m+m6)
elif m6 >= 65 <70:
    m=m6/100*1
    print("Added Attendence:",m)
    print("Total Average:",m+m6)
    M = m+m6 # added veriable for over all...
else:
    m=m6/100*0
    print("No Extra Attendence added:",m)
    print("Total Average:",m6)
    if M >= 95:
        print("Grade:A+")  # Grade not getting printed why ??????????
    elif M>=90 <95:
        print("Grade:A")
    elif M>=85 <90:
        print("Grade:B+")
    elif M>=70 < 85:
        print("Grade:B")
    elif M>=50<70:
        print("Grade:C")
    else:
        print("FAILED")'''
'''print('_______CARS__________________')
c=input("Car Colour:") #if we add extra variables will it occupy space...and will it effect on performance speed
c=c.title()
cc=int(50000)
c1=int(input("Car Price:"))
c2=input("City:")
c2=c2.title()
if c== "Blue":
    print("Extra:20,000")
    if c2=="Delhi":
        c3=c1/100*20
        c4=20000
        print("TAX:",c3,':Extra Charges:',c4)
        c5=c1+c3+c4
        print("Total:",c5)
    elif c2 == "Mumbai":
        c3=c1/100*22
        c4=20000
        print("TAX:",c3,";Extra Charges:",c4)
        c5=c1+c3+c4
        print("Total charges:",c5)
    elif c2 == "Hyderabad":
        c3=c1/100*55
        c4=20000
        print("Tax:",c3,";Extra Charges:",c4)
        c5=c1+c3+c4
        print("Total Charges:",c5)
    elif c2 == "Chennai":
        c3 = c1 / 100 * 18
        c4 = 20000
        print("Tax:", c3, ";Extra Charges:", c4)
        c5 = c1 + c3 + c4
        print("Total Charges:", c5)
    elif c2 == "Kolkata":
        c3 = c1 / 100 * 17
        c4 = 20000
        print("Tax:", c3, ";Extra Charges:", c4)
        c5 = c1 + c3 + c4
        print("Total Charges:", c5)

    else:
        c3 = c1 / 100 * 14
        c4 = 20000
        print("Tax:", c3, ";Extra Charges:", c4)
        c5 = c1 + c3 + c4
        print("Total Charges:", c5)
elif c == "Red":
    if c2 == "Delhi":
        c3=c1/100*20
        c4=25000
        print("Tax:",c3,"Extra Charges:",c4)
        c5=c1+c3+c4
        print("Total Charges:", c5)
    elif c2== "Mumbai":
        c3=c1/100*22
        c4=25000
        print("Tax:",c3,"; Extra Charges:",c4)
        c5=c1+c3+c4
        print("Total Charges:", c5)
    elif c2 == "Hyderabad":
        c3 = c1/100*55
        c4=25000
        print("Tax:",c3,";Extra Charges:",c4)
        c5=c1+c3+c4
        print("Total Charges:", c5)
    elif c2=="Chennai":
        c3 = c1/100*18
        c4 = 25000
        print("Tax:",c3,';Extra Charges:',c4)
        c5 = c1 + c3 + c4
        print("Total Charges:", c5)
    elif c2 == "Kolkata":
        c3 = c1/100*17
        c4 = 25000
        print("Tax:",c3,';Extra Charges:',c4)
        c5 = c1 + c3 + c4
        print("Total Charges:", c5)
    else :
        c3=c1/100*14
        c4=25000
        print("Tax:",c3,";Extra Charges:",c4)
        c5 = c1 + c3 + c4
        print("Total Charges:", c5)
elif c == "Yellow":
    if c2 == "Delhi":
        c3 = c1/100*20
        c4=30000
        print("Tax:",c3,";Extra Charges:",c4)
        c5=c1+c4+c3
        print("Total Charges:",c5)

    elif c2=="Mumbai":
        c3=c1/100*22
        c4=30000
        print("Tax:",c3,";Extra Charges:",c4)
        c5=c1+c3+c4
        print("Total Charges:",c5)

    elif c2=="Hyderabad":
        c3=c1/100*55
        c4=30000
        print("Tax:",c3,";Extra Charges:",c4)
        c5=c1+c3+c4
        print("Total Charges:",c5)

    elif c2=="Chennai":
        c3=c1/100*18
        c4=30000
        print("Tax:",c3,";Extra Charges:",c4)
        c5 = c1 + c3 + c4
        print("Total Charges:",c5)

    elif c2=="Kolkata":
        c3=c1/100*17
        c4=30000
        print("Tax:",c3,";Extra Charges:",c4)
        c5=c1+c3+c4
        print("Total Charges:",c5)
    else:
        c3=c1/100*14
        c4=30000
        print("Tax:",c3,";Extra Charges:",c4)
        c5=c1+c3+c4
        print("Total Charges:",c5) #do we need to stop here or end with else again if i end with else it showing error
else:
    if c2=="Kolkata":
        c3=c1/100*17
        c4="NA"
        print("Tax:",c3,';Extra Charges:',c4)
        c5=c1+c3
        print("Total Charges:",c5)
    elif c2=="Hyderabad":
        c3=c1/100*55
        c4="NA"
        print("Tax:",c3,":Extra Charges:",c4)
        c5=c1+c3
        print("Total Charges:",c5)
    elif c2=="Chennai":
        c3=c1/100*18
        c4="NA"
        print("Tax:",c3,":Extra Charges:",c4)
        c5=c1+c3
        print("Total Charges:",c5)
    elif c2=="Delhi":
        c3=c1/100*20
        c4="NA"
        print("Tax:",c3,":Extra Charges:",c4)
        c5=c1+c3
        print("Total Charges:",c5)
    elif c2=="mumbai":
        c3=c1/100*22
        c4="NA"
        print("Tax:",c3,":Extra Charges:",c4)
        c5=c1+c3
        print("Total Charges:",c5)
    else:
        c3=c1/100*14
        c4="NA"
        print("Tax:",c3,';Extra Charges:',c4)
        c5=c1+c3
        print("Total Charges:",c5)'''

print("------------------------------------------------")

b=(input('Enter Date Of Birth:'))
b1=b.split('/')
b2=int(b1[0])
b3=int(b1[1])  #month-int type...
b4=int(b1[2])
#m=['months',"January","February","March","April","May","June","July","August","September","October","November","December"]
#mn=m[b3]
b7=b3-1
m=["January","February","March","April","May","June","July","August","September","October","November","December"]
mn=m[b7]
print("Name of Month:",mn)
c=input("Current Date:")
c1=c.split("/")
c2=int(c1[0])
c3=int(c1[1])
c4=int(c1[2])
import calendar
print(calendar.month,(c3,c4))
age=c4 - b4
print("Age:",age)
if age <=5:
    print("You are eligilble for Scholarship of 20,000/-")
if age>5 and age<=10:
    print("you are eligible for Scholarship of 30,000/- ")
if age >10 and age<=15:
    print("You are eligible for Scholarship of 40,000/-")
if age >15 and age<18:
    print("you are eligible for scholarship of 50,000/-")
if age >18:
    print("Not eligible for Scholarship")


print("--------------------------")

'''p=input("Enter City:")
p5=input("Category")
p.title()
p1=int(input("Enter Units:"))
if p== "Delhi":
    if p1>=200:
     print("Free")
    elif p1>200 and p1<=300:
        p3=p1*8
        print("Total Amount:",p3)
    elif p1>300 and p1<=500:
        p3=p1*12
        print("Total Amount:",p3)
    else p1>500:
        p3=p1*15
        print("Total Amount:",p3)
elif p=="Chennai":
    if p1>=100:
        print("Free")
    elif p1>100 and p1<=200:
        p3=p1*6
        print("Total Amount:",p3)
    elif p1>200 and p1<=400:
        p3=p1*10
        print("Total Amount:",p3)
    else p1>400:
        p3=p1*12
        print("Total Amount:",p3)
elif p=="Hyderabad":  #free power for farmer....
    if p5=="Farmer":
        print("No Charges:")
    elif:
    if p1 >= 150:
        print("Free")
    elif p1 > 150 and p1<= 300:
        p3 = p1 * 8
         print("Total Amount:", p3)
    elif p1 > 300 and p1<= 500:
            p3 = p1 * 10
            print("Total Amount:", p3)
    else p1 > 500:
            p3 = p1 * 12
            print("Total Amount:", p3)

else:
    if p1>=250:
        print("Free")
    elif p1>250 and p1<=400:
        p3=p1*10
        print("Total Amount:",p3)
    elif p1>400 and p1<=550:
        p3=p1*14
        print("Total Amount:",p3)
    else p1 > 550:
        p3=p1*18
        print("Total Amount:",p3)'''









