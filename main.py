# python has bytecode which run on python virtual machine high level lang can provide control
# has community and is portable

# powerful
# extend the code using other langs if needed and has low level support too
# python is extensible (written in c)


# maths
# numpy for calc
# text processing rapid app development  cross platform development
# u can extend the functionalities of the os
# database programming
# extensions there for every thing in python
# python does compile the code into bytecode but it is handled by the interpreter

# u can execute a line of code in the interpreter directly(shell)
# file is module anc can be called scripts cause its scripting

# types of python are objects

# number string  list dictionary tuple file

# integer = 12345
# float = 123.45
# string = "hello"
# list = [1, 'Two', 2]

# tuple = (1, 'tow', 23)


# operators
# or
# lambda
# and not is is not in not in x |y x^y  & << >>
# + - * / %
# [] [:]

# number
# ox for hexadecimal
# long integers just append L to the end of the number

# floatiing number uses double as base
# floats are repsreentaion of the number they represent precision upto 15 decimal places
# cplx = 1 + 3j

# + -  * / % ** -x +x  we have the augmemnted operator for the same as well
# << >> & | ^ ~ \\

#  numberic functions
# abs(x)
# coerce(x,y)
# divmod(x,y) tuple with quotient and the remainder

# pow(x,y)
# round(x,y)


# strings :=
# strings are immutuable
# ''"" ''''''
from math import gcd
import numbers
import os as o  # aliasing
import sys
s = 'I''am'
print(s)  # Iam

# len() //the value of the length
# s *5  //n times add
# s+s  //concatenate them
# s+ 5//error


# s[0] //first index as as strings are arrays
# slicing
# s[0:10]
# s[:]
# s[:4:-1]//reverse

# -ve value from the end
# -1 for last element
# s[-1]


# formatting in python

album = {'title': 'Flood', 'id': 56}

# print("catalog number %(id)05d is %(title)s" % album)
# escape characters

#  raw strings
# print(r'\a\n\x99') //prints the same string r or R


# lists are sequence mutable

list = [1, 2, 34]
# they basically store the objects how it could be implemented
song = ['a', 'b', 43]
# array of base class and pointers pointing to the obj having virtual functions
list = list+song
song += ['aka']

list *= 2

print(list)

# list comphersion
list = [x ** 3 for x in range(1, 10)]
print(list)

# lists are mutable
# del list
list[3:4] = [4, 8]
print(list)

# list methods
# list.append(x)
# list.count(x)
# list.extend(L)
# list.insert(i, x)
# list.pop()
# list.remove(x)  # deletes the first occurrence
# list.sort()

# None complement of NULL


# tuples
# tuples are immutable

# one= (1)3 value 1
one = (1,)  # tuple

# u can change the tuple but not the values inside them

# membership operators
# in not in
# is not is

# for day in days:
# print(day)


# dictionary
# key value pair key is immutuble while value can be changed

album = {'flood': {1: "birdhouse in your soul "}}

album["flood"]

# if key not found the dictionary raises dictionary methods exception

del album['flood']

# dictionaries have no order

keys = album.keys()
values = album.values()


# methods
album.has_key(x)
album.keys()
album.values()
album.items()
album.clear()
album.update(x)


# files
# ope
# ()

# object storage
# python stores info as objects

getting = "hello"
# somewhere exists a object that stores the values hello and is pointed byt teh gretting
# when we reassign the pointer now pints to the new object
# rules for var naming
# no keywords
# start with underscore or letter
# case sensitive

# python copies refrences not the data
objecta = [1, 23, 4]
objectb = objecta
objectb = [12]  # now this is not working

print(objecta)
objecta = [12]
print(objectb)

# objectb is always pointing to the objecta so any chang ein value of a
# is seen in b b

# it becomes easier to nest as we have pointer in there not teh actual copy

# type conversion
a = 10
print(f"{a}")

# str()
# print(`expression `) evaluate the exprssion and return the result as string
# str(x)
# list(X)
# tuple(x)
# long(x)
# int(z)
# complex(x,y)
# float(x)
# oct(x)
# hex(x)
# min(iterator)
# max(iterator)
# chr(x)
# ord(x)


# comparison
a = [1, 4, 5]
b = [1, 4, 5]
print(a == b)  # true order as well as values \
# is to check if its pointing to same object
# x<y<z
# x<>y similar to x!= y
#
# dictionary are compared by the sorted key/value pair

print("akdklfakldjfakl \
  fmkadfakldfkald adfa \
    dfafa")

# comments
title, name = 'mr', 'martin'

# tuple assingment and list assignment
# swap
title, name = name, title

# multi target assignment
group = a = "aksns gsjfsfkjsk;ls"


fp = open("newfile.txt", "w")
sys.stdout = fp  # changing the standard mode of print output
print("hello newfile")


# complex types are printed as strings as well

# control statement
# if (conf):
#     dfak
# elif (fakd):
#     falkd
# else:
#     ldaf


# never forget indention here
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a Blockchain developer")


match lang:
    case 1:
        print(1)
    case 2:
        print(2)


# while(expression):
#   #code
# else:
#     #block

# for target in objext:
  # do something

# ranges

# range(start,stop,step)

# break
# continue

# pass
# functions
def name(name, *args):
    # body of the function
    pass


# scoping
# python has namespaces where it stores the values of the functions

# global scope
# any var defined in the local scope is locall until defined with the global keyword


# local global then built in
# function inside functions
# child dont inherit the vars of the parent function

def func():
    value = 59
    funcb()

    def funcb(value):
        # this is gonna givce error better way is to pass teh value as a parameter
        print(value * 3)


# arguments are copied by reference into local object
# the original var are not modified from the changes inside the function

# reference data type can have their values changed list tuple dictionary


list = [1, 2, 3]


def modi(list):
    list = [2, 3, 4]


modi(list)
print(list)


def mdod1(list):
    list[0: 3] = [4, 5, 6]


mdod1(list)

print(list)  # the value of teh list changes in this case

# you cannot the change the real object but modify the mutable objects inside the functions

# arguments are objects

# keyword arguments


def multiply(a, b):
    print(a)


multiply(3, 2)
multiply(b=3, a=2)  # works


# default arguments
def a(b=3, c=4):
    print(c, b)


a(54, 54)
a()


# arguments tuples
def alf(list, *args):
    for item in items:
        list.append(item)


# argument dictionary
def message(text, **kwargs):
    for key in kwargs.keys():
        print(text, kwargs[key])

# default arguments after non default arguments

# return values


def sqsq(first, second):
    first = first * first
    second = second ** 3
    return first, second


s, c = sqsq(3, 4)

print(s, c)


# other functions
# apply(multiply, (1, 2)) shifted to pandas


def cube(x):
    return x ** 3


map(cube, list)

# functions are objects as well
x = cube
print(x(3))

# anaymous functions lambda

# f = lambda x: x *x
# modules in python


try:

    import matplotlib
except ImportError:
    print("hell something is fishy here and missing too")

# import pandas

# importing functions specifically

# reload(sys) #force the interpreter to reinterpret the module
print(sys.path)

sys.path.append("./WEEK1")
print(sys.path)
sys.path.insert(0, "../ENGLISH1")

if __name__ == "__main__":
    print("script")
else:
    print("module")

# packages group of modules placed and grouped together
# create __init__.py  inside the package
# //#object oriented

# classes objects instance of object
# inheritance


class Account:
    account_type = 'Basic'

    def __init__(self, name, balance):  # constructor
        self.name = name
        self.balance = balance
  # when the refrence count reaches 0 the object si auto deleted /
  # but we can have our constructor  __del__()

    def depsoit(self, value):
        self.balance += value

    def withdraw(self, value):  # self refers to the object created with
        self.balance -= value


bank = Account('HSBX', 300)

# class members class methods

# sepcial methods

# __init__(self,args)
# __del__(self)
# __repr__(self)/
# __str__(self)
# __add__(self,other)
# __cmp__(self)
# __hash__(self)
# __nonzero__(self)


def __str__(self):
    return "%s: %g" % (self.name, self.balance)
