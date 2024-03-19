#variables and the different data types
student_name="kamau" #string
student_age=20 #integer
student_height=7.5 #float
"""
print(student_height)
print("my students name is:",student_name)
print("kamau age is:",student_age)
#print(student_name,student_age,student_height)

firstname="the name of my student is kamau"
secondname=100
fullname=firstname+" "+str(secondname)
print(fullname)

price1="200"
price2=500
#total=price1 + price2
total=int(price1)+price2
print(total)

#OPERATORS
#Arithmetic operators
# + - * / % ** //

#print(2/5)
print(2%5)
#print(2%5)

#checking if a number is odd or even
y=20
#print(y%10)

if y%2==0:
    print("even")
else:
    print("odd")


#assignment operators
z=6
z+=4  #z=z+4
z%=5
print(z)

#comparison operators
print(5!=2)
print(5==2)

#logical operators
#and or
age=20
nationality="north america"
if nationality=="kenya" and age==35:
    print("you can be president")
else:
    print("you can't be president")

x=30
if x%2==0:
    print("even")
else:
    print("odd")

#illustrattion of the elif
z=5
if z>3:
    print("the value in z is greater than 3")
elif z==3:
    print("the value of z is equal to 3")
else:
    print("the value of z is less than 3")

#checking the city of our candidate
#city=input("enter your city name:")
#if city=="mombasa":
  #  print("elligible")
#elif city=="nairobi":
   # print("elligible")
#elif city=="machakos":
 #   print("elligible")
#else:
 #    print("not elligible")

y=int(input("enter your first number:"))
x=int(input("enter your second number:"))
user=str(input("enter your choices:"))
if user=="add":
    total= x+y
    print(total)
elif user=="mutiply":
    total= x*y
    print(total)
else:
    total= x-y
    print(total)
"""
"""
#continue and the break statement
x=1
while x<=10:
    if x==3:
        x += 1
        continue
    print(x)
    x+=1
print("end of break statement")

y=3
while y<=10:
    print("the value of y is:",y)
    y+=1
else:
    print("loop ended")

x=0
sum=0
while x<=10:
    if x%2==0:
        x=x+1
        continue
    else:sum=sum+x
    x=x+1
else:
    print(sum)
visitors=int(input("enter the number of visitors:"))
uganda=0
kenyan=0
counter=1
while counter<=visitors:
    nationality=input("enter the nationality:")
    if nationality=="kenyan":
        kenyan+=1
        print("allowed")
        counter+=1
    else:
        uganda+=1
        print("not allowed")
        counter+=1

print("the number of visitors is:",visitors)
print("the number of kenyans is:",'kenya' )
print("the number of ugandans is:",'uganda')

#for loop implementation
cars=["car","bus","car"]
for car in cars:
    print( car)

for x in range (3):
    print("yng")

#even numbers
sum=0
for x in range(1,11):
     if x%2==0:
         sum=sum+x
print("sum of even numbers:",sum)

#data structures
mystudents=["ethan","john","michael"]
print(mystudents)
mystudents.append("moses") #adding
print(mystudents)
mystudents.remove("michael") #removing
print(mystudents)
mystudents.remove(mystudents[1])
print(mystudents)
mystudents[0]="ethan2.0"  #modifying
print(mystudents)
                                       
#student list
students=[]
student1=input("enter the first")
print=("you have entered the name:",student1)
students.append(student1)

student2=input("enter the second")
print=("you have entered the name:",student2)
students.append(student2)

student3=input("enter the third:")
print=("you have entered the name:",student3)
students.append(student3)
print(students)

#lists 2.0
students=[]
print("enter 5 names:")
for students in range(5):
    students=input("enter name")
    students.append("students")
print("list of students:",students)
"""
#tuples
mytuple=("ethan","john","michael")
#properties of tuples
"""
1.tuples are immutable ie they cannot be changed directly
2.elements in tuple are indexed 
3.tuples are usually round brackets
4.tuples allows duplicates
5.tuples can have elements of different data types
"""
"""
print(mytuple[1])
mytuple[1]="john" #this will give an error because we cannot change tuples directly
print(mytuple[1])
"""
#to modify/add/delete tuples
"""
1.convert the tuple to list
     mylist=list(thetuplename)     
2.modify the value you wanted the same way we did in lists
     example on modifications:
           student[0]="ethan"
     example on deleting:
           student.remove(student[0])
      example on adding:
            student.append("moses")
3.convert it back to a tuple 
     mytuple=tuple(thelistname)                                           
"""
