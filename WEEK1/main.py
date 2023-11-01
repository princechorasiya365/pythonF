# //intro to week 1
print("hellowordld", "prince")
# //numbers fractions  string everything can be printed here
a = 10
b = 20
print(a)  # assign and print
print(a+b, a*b)

a = int(input())  # take input form user
print(a)


print("Enter your name:")
name = str(input())
print(name)
print("how are you ", name)


st = "abc  "
st = st.strip()
print(st, "pc")

age = int(input("enter your age: "))
print(age)
# variables are containers whose value can be changed
# "sudharshn " #literals  /
age = age + 1  # possible
# 30 + 30+1 //wrong
# literals only on right use when we need constant values

r = int(input("Enter the value of radius: "))
area = 3.14 * r*r

print("The area of the circle is ", area)


n = 10
print(n)

r = 6.3
print(r)
s = "prince"
print(s)
print(type(n))  # prints the value of the type of value stored in the n
print(type(r))
print(type(s))
l = [1, 2, 3, 4]
print(l)
print(l[0], l[1])
print(type(l), type(l[0]))


# //data type 2
b1 = True  # boolean data type
b1 = False
print(type(b1))

# conversion
a = int(5.7)
b = int('10')
print(a, type(a))
print(b, type(b))


# integer to flaot
a = float(9)

print(a, type(a))
a = str(9)
print(a, type(a))

# type casting

# bool data
a = bool(10)

b = bool(0)  # false other are true
b = bool("str")  # only null stirng is false
print(a, b)


# //operators 
+ - * /(float output) //(int output ) %  ** 


# string concatenation 
# a+b both have to be string 
# list +list 
# concatenate both 
# //operator precedence 

# arithematic 

# relaitional  output is boolean
# >= > <= <= == != 
print(5>5) #false
# logical 
# and or not 
# shortcircuiting is always there 


# intro to string
s = "coffee"
t = "bread"
print(s)
print(t)
print(s+t)
print(s[0], s[1], s[-1])
print(s[0:9])  # // no overflow
# include first index and exclude last index string slicing

# shift + .
# shift  + , fro speed change

a = s[0]

s = "a"
print(s*5)  # replication
x = "india"
print(x == "india")
print(x == "India")
print("a" > "b")  # compare
print("4" > "10")  # string comparison using character by character


# string indexing -ve indexing start from -1 last element
# -1 to n n size of string
# print(s[2])  # index error 
# print(len(s))  #print length of the character  0 to s-1 indexing 



a = 0 
#sum of factoial of number upto n 
n = int(input())
for i in range(1, n + 1):
    b = 1
    for j in range(1, i + 1):
        b = b * j
    a = a + b
print(a)
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

S = 0
while len(L) >= 2:
    S += L[0] + L[-1]
    L = L[1:]
    L = L[:-1]