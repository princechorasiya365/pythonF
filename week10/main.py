# object oriented programming  
# considers every entity as objects 
# which have attribute and function(behaivour defined on them )
# buleprint and that is shared with others 
# //attribute and behaviour every object must have its own identtity 
# to mainatin uniformity we use base blueprint this blueprint is called class 
# //blue prints then create object and name them whatever we want 

class Student:#class name first letter captial 
  roll_no =None
  name = None

s0 = Student() #looks like a function call this is a special type name identical to name of the class used for creating the constructor 

s0.name ="prince"
s0.roll_no =0
print(s0.roll_no,s0.name)

# create object using constructor then set values to the needed name using operator 
# we use . operator to access anything insdide a class 
# None and None are default values inside the class 

# each object has its unique identity 

s2=  Student()
s2.name ="liza"
s2.roll_no = 6
print(s2.name,s2.roll_no) 
# we ccan create and indefinate amount of objects as per or needs 

# smae vairable anme for each object 


# behaviours 
# functions of the class 

# //behavour funnctions 
# object blueprint of class 

# behaviour part of object 

class Student:
  count =0 #belong to the class static we can use this to create teh count of object created 
  def __init__(self,name,roll_no): #the constructor of the class  variable inside the init belong to object 
    self.name = name
    self.roll_no = roll_no
    Student.count += 1
  def display(self):
    print(s0.roll_no,s0.name,Student.count) #error here we gotta us self no s0


#self keyword to refer to the object created self is going to refere which object initiated the transaction 
# container that hold the current object 



s0 = Student("prince",1)
s0.display()

s1 = Student("prince",4)
s1.display()
#done using constructor as automatically called after  execution 

# used along with functions 
# function variable and object variables  function belonging to a class is called method 


#inhertience and function overriding 
# child aquirung properties of parents 

# obtain properties overide them and add new things 

class Student:
  def __init__(self,name,roll_no,age):
    self.name =name
    self.roll_no = roll_no
    self.age =age
  
  def dispaly(self):
    print(self.roll_no,self.roll_no,self.age)

class Employee:
  def __init__(self,name,age,salary):
    self.name =name
    self.age =age 
    self.salary =salary
  
  def display(self):
    print(self.name,self.age,self.salary)


# //a lot of repetion to prevent this repetiion for various use we dont repeat the same class eveytime 
# instead we just create them from a base class 



class Person: #parent class superclass 
  def __init__(self,name,age):
    self.name = name 
    self.__age = age
  
  def display(self):
    print(self.name,self.__age) 

class Student(Person):
  def __init__(self,name,age,marks):
    super().__init__(name,age)
    self.marks = marks 
  
  def display(self):
    super().display()
    print(self.marks)

class Employee(Person):
  def __init__(self,name,age,salary):
    super().__init__(name,age)
    self.salary = salary
  
  def display(self): #method overridding 

    print(self.name,self.__age,self.salary)
# __employee __not accessible 

s0 = Student("prince",18,98)
e1= Employee("empl",19,9999999)
s0.display()
e1.display()



# 3importing form other files 
# from Student import Student place them on their files and import them 

# no privacy till now 
# no access modifiers till this 
# __ private 

# types of inhertience 
# simple (parnet child)

# heirachical (parent child1 child2) 
# mulitple inheritenee(2parent 1 child) 
# multilievel inheritence (grandparent parent child)
# hybrid inhrtience 



# numpry lib processing library 

import numpy as np 

a =[42]

b =[1,2,3]
c= [[1,2,3],[1,2,3]]
d = [[c,c,c]]
print(a)
print(b)
print(c)
print(d)
a = np.array(a)
b = np.array(b)
c = np.array(c)
d = np.array(d)

print(a,a.ndim)
print(b,b.ndim)
print(c,c.ndim)
print(d,d.ndim)

# uses n dimensional array 
# numpy numerical python 

# array c wala list can have many types 
# nested list are still 1d linear 

# intro to matlab 
# matplot lib to visualize 
import matplotlib.pyplot as plt
import numpy as np

x= np.array([1,2,3,4,5,6,7,7,8,9,10])
y = np.array([1,2,3,4,5,6,7,8,9,10,11])
z =np.array([2,3,4,5,6,7,8,9,10,11,12])
a = ["a","b","c","e","d","f","g","h","i","j","k"]
plt.scatter(x,y)
plt.hist(x)
plt.pie(y,labels =a ,startangle=90)

# we can create subplot for each of this subgraphs 
plt.subplot(2,3,1) #creates 2 *3 grid and the last position is the element to be replaced 
plt.scatter(x,z)
plt.show()



class Student:
    count = 0
    def __init__(self, name, roll, maths, physics, chemistry):
        Student.count += 1
        self.roll = roll
        self.name = name
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry

class Group:
    def __init__(self):
        self.members = [ ]

    def add(self, student):
        self.members.append(student)

    def print_members(self):
        for student in self.members:
            print(student.name)

studnet = Student("snish",4,65,45,34)
