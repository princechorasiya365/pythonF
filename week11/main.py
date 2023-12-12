# //exception handling  and functional programming ()

# exception what and why 
a = int(input())
b= int(input())


#no error in the code works fine but stucks in one condition 
#b=0 division by zero 

# error(syntax error) and exception are different 

# namerror zerodivisionerror filenotfounderror 
# exception when our syntax is correct but not the desired result due to logical errors are exceptions //

# handling this exception 
# terminate the prograrm with a usefule error message guided message to user so he can prevent wrong values 
# finding exceptions 
try:
  c =a/b
  print(c) #name error we should handle nameerror as well
  f = open("file.txt","r")
except ZeroDivisionError: 
  print("Divisor cannot be zero enter again ")
  # pass #use when syntax is necessary but we dont want to anything htere 
except NameError:
  print("vaeiable not defined")
except FileNotFoundError:
  print("file not found change the file name")
except:
  print("somehting went wrong") #whenn no execption from the list are found 


# somthing not predefined errors 

# error occurs break the try and move to except and check one by one match and print the error message and then exit 
# what happended to variable inside the try 
# for example f =open("") remains still open we have to close 
# that file 

# finally block 
try:
  f =open("abc.txt","r")
  c =5/0
  print(c)
  # f.close() #instead of closing it here we close it in finally block
except ZeroDivisionError:
  print("Dividing by zero")
finally:
  f.close() #excute always doesnt matter exception or not 
  #what happens if exception in finally block 


# user defined exception 
a= int(input())
if a<18:
  print("you are underage,cannot vote ") 
  raise Exception("you are underage,cannot vote") #first line to be executed 


# functional programming 
fruit =[1,2,3,4,5,6]
for f in fruit:
  print(f)

# //have a basket and distribute them 
# sleep for making program wait  as we may not find the child instantenously 

basket = iter(fruit) #cerbaskateing a iterator 
print(basket)
print(next(basket)) # 1
print(next(basket)) #2 
# //distribute tehm when we come across a kid 
# convert iteratable entity to iterator  

# for loops used the same concept 

# generator to generate the iterator 

def square(limit): #generator generates the iteratior 
  x=0
  while(x<limit):
    yield x *x 
    yield x **3
    x+=1
  

s =square(6)
print(s)
print(next(s),next(s))
print(next(s),next(s))
print(next(s),next(s))
print(next(s),next(s))
print(next(s),next(s))

# inline statments 
a =10
b= 20
if(a<b):
  small =a
else:
  small =b 
print(small) 

# replacing teh above code by using inline operators 
small = a if a<b else b  #performance is same as well 

print(small)

a =0
while (a<9):
  print(a)
  a+=1


while a <8 :print(a); a+=1

# //for loops 
# list comprehension 

fruits = ["ab","bc","ca"]
newlist = [fruit.capitalize() for fruit in fruits if 'b' in fruit ]
print(newlist) #list comphrenshion 
