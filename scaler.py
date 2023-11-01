# //indentation of python
import sys
import keyword
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the second number: "))

my_sum = num1 + num2
print("The sum if the 2 numbers is ", my_sum)

# //easy to learn easy to code interpreated language
# free and open source
# object oriented cross platform
# extensive fatures high level language database support gui program language standard lib
# dynamic typed language


# //application
# web (front and backend flask and django
# games (pygame(2-d )  pysos(3-d))
# gui app(tkinter,pyqt,kivy)
# calcualtions/ (scipy numpy pandas)
# ai and ml (tensorflow pytorch keras sckit learn)
# software developement
# bussiness application
# audio and video app(timPlayer Cplay)
# other languages
# scrapping sites( BeautifySoup Scrapy Requests Selenium)

# CAD app of python
# image processing
# writing scripts


# //indentaion to represent the block of code
# interactive mode (shell
# script mode write the file and then execute )

# indentation
if True:
    print("Bye")
# keep indent uniform

# identifiers
# (a-z A-Z 0 -9 _)
# identifiers cannot start with numbers
# case sensitive
# length of the variable no restriction

print("var".isidentifier())
# isidentifier()
# kwywords for python
print(keyword.kwlist)
print(keyword.iskeyword("prince"))

# //comments in python
# single line
"""multi line comment
"""

message = "This is a long statement that I want to write, but the " \
          "problem is that it doesn't fit in one single line. So this is how " \
          "I've written it for readability."

# //multi line string
a = 1
b = 2
c = 3
# a=1;b=2;c=3 //same as above

# quot '' "" """ """


# //arguments
# python code.py arg1 arg2 ...argN


# sys module

if len(sys.argv) != 3:
    raise ValueError("provide your name and age")

print(f'your name is {sys.argv[1]} and your age is {sys.argv[2]}')
# python runner.py prince 12
# pip -V pip is mandatory
# sudo yum install python

# //difference btw 2 and 3
print("python version is ", sys.version[:3])
print(type(1))

# //basic syntax visualization
# //develop serialized resumes for different job profiles

name = "rahul"
if name == 'rahul':
    print('welcome rahul')
    print('how are you')
else:
    print('duse fuck of i')
    print('why are u here')

print('have a great day')

i = 1
while (i <= 6):
    print("value is  "+str(i))
    i += 1


number = 50
if (number != 0):
    if (number % 2 == 0):
        print("given umber is even")
    else:
        print("given number is odd")
else:
    print("given number us neither even nor odd")


# //indentation error 
if (l==1):
print("test code ") #this wont work  
  print("this is test code1") #error here as well 


# variables python containers for storing the variable 
value =111
print("Value a per the first declartion: ",value);
value = 222
print("Re-declared value: ",value);


num1 = num2 = num3 = 1052

print(num1, num2, num3)
whole_number, stri, decimal = 10, "hello world", 22.50

# types of var
# scope rules
no = 10
del no  # no is not defined from this point
print(no)

# every object belongs to a specific class 
# variable points to the space in the main memmory 

# //no two variable can have same i 

print(id(no))


# keywords and identifiers 
# builtin functions 

