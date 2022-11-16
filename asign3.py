print('-----------Replace---------')

# Replace
s1= '''apple is a fruit
      apple is red in color
      apple is healthy
      apple keeps doctor away
      apple grows in cold area'''

print(s1)
print('__________________________________________________________________')
res=s1.replace("apple","mango",4)
print(res)
print('____________________________________________')
res1=res.replace("mango","grapes",1)
print(res1)
print('________________________________________________')
res2=res1.replace("mango","orange",1)
print(res2)
print('______________________________________________________')
res3=res2.replace('mango','banana',1)
print(res3)
print('_______________________________________________')
# List to String.
q=(['apple','mango','banana'])
print(q)
print(type(q))
res=''.join(q)
print(res)
print(type(res))
print('_________________________________________________')
email="arjun.2010@gmail.com"
res=email.split("@")
print(res)
res1=res[0].split('.')
print(res1)
res2=res1[0]
print(res2)
res3=2022
res4=int(res1[1])
res5=res3-res4
print(res5)
res6='www.'
res7=res6+res[1]
print(res7)
print('name:',res2)
print('age:',res5)
print('domain:',res7)

print('___________________count______________________________')
a2="35 apples price 1245 price 25 oranges 824"
ra2=a2.split(' ')
print(ra2)
ra3=int(ra2[0])
print(ra3)
ra4=int(ra2[5])
print(ra4)
print("fruits sold")
ra5=ra4+ra3
print(ra5)  #total pieces of fruits
   #total money gained..
print('money gained')
ra6=int(ra2[-5])
#print(ra6)
ra7=int(ra2[-1])
#print(ra7)
#print(type(ra6))
#print(type(ra7))
ra8=ra6+ra7
print(ra8)

print('_________________suresh.1999@ibm.com___________________________')
print('ASSIGNMENT1')
#suresh.1999@ibm.com
mail=input("Enter your mail:")
print(mail)
rs1=mail.split('.')
print(rs1)
rs2=mail.split('@')
print(rs2)
rs3=rs1[1].split('@')
print(rs3)
#rrs3=rs3[0]
#print(rrs3)
#fres="".join(rs2[1])
#print(fres)
rs4='www.'
fres1="".join(rs4)
#print(fres1)#adding domain site
rs5=fres1+rs2[1]

a=int(rs3[0])
#print(a)
b=2022
c=b-a
#print(c)
#rs7=rs6-rs3
#print(rs7)
print("Name:",rs1[0])
print("Domain:",rs5)
print("age:",c)

print('____________arjunyadavgolla.2015@gmail.com______________________')
#arjunyadavgolla.2015@gmail.com
email=input("enter you mail:")
print(email)
e1=email[0:5]
#print(e1)
e2=email[5:10]
#print(e2)
e3=email[10:15]
#print(e3)
e4=email[16:20]
e9=int(e4)
#print(e9)
e5=email.split('@')
#print(e5)
e10="www."
e11=email[21:30]
#print(e11)
e12=e10+e11
#print(e12)
e6=email.split('.')
#print(e6)
e7=2022
e8=e7-e9
print('First Name:',e1)
print('Last name:',e2)
print('Surname:',e3)
print("Age:",e8)
print("Domain:",e12)
print('_____________Accept student details________________________')
#Accept student Details...
m6=input('Enter Student Name:')
m7=input('Enter Student Class:')
m1=int(input('Enter English Marks:'))
m2=int(input('Enter Science Marks:'))
m3=int(input('Enter Social Marks:'))
m4=int(input('Enter Maths Marks:'))
m5=int(input('Enter Computer Marks:'))
m8=m1+m2+m3+m4+m5
print(m8)
m9=m8/5
print(m9)
#out put to show marks..
print('--------out put marks---------------------------')
print('Name:',m6)
print('class:',m7)
print('English:',m1)
print('Science:',m2)
print('Social:',m3)
print('Maths:',m4)
print('Computer:',m5)
print('Total Marks:',m8)
print('Average:',m9)
print('-------------accept employee details----------------------')
#Employee Details................

em1=input('Enter Employe Name:')
em2=input('Enter Technology:')
em3=input('Enter Designation:')
em4=int(input('Enter Salary:'))
em5=em4*(30/100) #added bonus as 30% of salary...
print(em5)
#
print('---Out Put----------')

print('Employe Name:',em1)
print('Technology:',em2)
print('Designation:',em3)
print('Salary:',em4)
print('Bonus',em5)


print('_____________split________here i have errors4._____________')
'''d1= " usa india uk india france india japan" #is this correct.....
print(d1)
print(type(d1))
print(len(d1))
d2=d1.find('india')
print(d2)
d3=d1.find('india',d2+1)
print(d3)
d4=d1.partition('india',[d3])
print(d4)
print(type(d2))
d3=str(d2)
print(type(d3))
d4=d3.partition('13')
print(d4)'''
#d3= str(d2)
#print(d3)
#d4=d1.partition('india',d3 +1)
#print(d4)
#d2=d1[14:20]
#print(d2)
#print(type(d2))'''