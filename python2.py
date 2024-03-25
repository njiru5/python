#classes and objects
class student:
    admissin_number=''
    student_name=''
    student_age=''
    def __init__(self,admission,name,age):
         self.admission_number=admission
         self.student_name=name
         self.student_age=age
         print('student:',self.admission_number,self.student_name,self.student_age)

student1=student(7215,'ethan',18)
student2=student(7498,'moses',19)
#
class student:
    admissin_number = ''
    student_name = ''
    student_age = ''
    def __init__(self):#constructor gets called by default whenever an object is created
        print("init student class")

    def set_name(self,name):#setting the name
        self.student_name=name
    def display_name(self):#displaying the name
        print("student name:",self.student_name)

student1=student()
student1.set_name('john')
student1.display_name()
#inheritance
class person:
    person_age=0
    person_name=""
    person_residence=""
    def __init__(self,name,age,residence):
        self.person_name=name
        self.person_age=age
        self.person_residence=residence

    def printperson(self):
        print("name:",self.person_name,"age:",self.person_age,"residence:",self.person_residence)
#inheriting from the parent class
class student(person):
    uniform=""
    def __init__(self,name,age,residence,uniform):
        super().__init__(name,age,residence)
        self.uniform=uniform

class teacher(person):
    pay=0
    def __init__(self,name,age,residence,pay):
        super().__init__(name,age,residence)
        self.pay=pay
teacher1=teacher("kelvin",19,"nairobi",1200)
teacher1.printperson()
print("pay:",teacher1.pay)

#inheritance 2
class person:
    person_age=0
    person_name=''
    person_residence=''
    def __init__(self):
        print("name:",self.person_name,"age:",self.person_age,"residence:",self.person_residence)
    def set_values(self,person_age,person_name,person_residence):
        self.person_age=person_age
        self.person_name=person_name
        self.person_residence=person_residence

person_instance=person()
person_instance.set_values("19","ethan","nairobi")
print("age:",person_instance.person_age,"name:",person_instance.person_name,"residence:",person_instance.person_residence)
#polymorphism
class animal:
   def __init__(self):
       pass
   def speak(self):
       print("I am animal and i speak")

class dog(animal):
    def __init__(self):
        pass
    def speak(self):
        print("I am a dog and i bark" )

class cat(animal):
    def __init__(self):
        pass
    def speak(self):
        print("I am a cat and i meow")

dog1=dog()
dog1.speak()

cat1=cat()
cat1.speak()