#sets
mystudents={"alex","bruno","james","james","michael" }
print(mystudents)
for student in mystudents:
    print(student)
#dictionaries
#data is stored in key value pairs
#ie key:value
cardata={
    "model":"mercedes",
    "brand":"sl amg 500",
    "yom":2015
}
print(cardata["brand"])#accesing values in a dictionary we use the key
cardata["alloys"]="contains"#adding data to a dictionary
print(cardata)

cardata["brand"]="sls 200"#modifying
print(cardata)

#functions
def is_even(number):
    if number % 2 == 0:
        print("even number")
    else:
        print("odd number")
#calling a function
is_even(99)
#function 2
def printemobilis():
    for i in range(10):
        print(i+1,"emobilis")

printemobilis()
#function 3
def printname(x):
    for i in range(10):
        print(x)
printname("ethan")
printname("moses")
#function 4
def getmodulus(y,x):
    return y%4

z=getmodulus(5,2)+90
print(z)
