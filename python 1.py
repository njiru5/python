#variables and the different data types
student_name="kamau" #string
student_age=20 #integer
student_height=7.5 #float



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