# //birthday paradox searching sorting  multiple matrix
import numpy
import math
import random
l = [1, 7, 5, 4, 53]
print(l)
l.append(1023)
l.append(1024)
# //dulicates allowded
l.remove(1)
print(l)
# remove removes the first occurence of the number

# //matrix

# nesting list
x = []
x.append(l)
x.append(l)
print(x)

m = []
m.append([1, 2, 3])  # m[0]
m.append([4, 5, 6])  # m[1]
m.append([7, 8, 9])  # m[2]
# list of list 2 d
print(m)


# /birthday parradox
# //birthday paradox

# print(random.random())
l = []
# create a list
# append 30 random number btw 1 to 365 //representing the day
# scientific simulation
for i in range(100):  # the more the peopke the more the probability of repetition
    l.append(random.randint(1, 365))

# //write a cod eto chekc for repition
l.sort()
flag = 0
print(l)
i = 0
while (i < len(l) - 1):
    if (l[i] == l[i+1]):
        print("repeats", l[i])
        flag = 1
        # break #check for other repetition
    i += 1

if (flag == 0):
    print("does nt repeat")


# //simulation


# l.sort()


# //search
# //search in list
l = []
for i in range(1000000):
    l.append(random.randint(1, 1000000))


while (True):
    a = int(input("Enter a number to be searched: -1 to exit  "))
    if (a == -1):
        break
    # print(l)
    flag = 0
    for i in range(len(l)):
        if (a == l[i]):
            print("found")
            flag = 1
            break

    if (not flag):
        print("not found")


# //sortr
l = []
for i in range(100):
    l.append(random.randint(1, 100))
# print(l)
# sort the obvious way
x = []
# find the min element
# put to x
# remove from l
while (len(l) > 0):
    mini = l[0]
    for i in range(len(l)):
        if (mini > l[i]):
            mini = l[i]

    x.append(mini)
    l.remove(mini)

print(x)


# //simulate birthday paradox to multiple time
# //code the birthday paradox

k = 0
r, nr = 0, 0
# while (k < 2):
while (k < 1000000):
    l = []
    for i in range(50):
        l.append(random.randint(1, 365))

    l.sort()
    flag = 0
    print("round ", k+1)
    # print(flag)
    for i in range(len(l)-1):
        if (l[i] == l[i+1]):
            # print("repeats", l[i])
            flag = 1

    if (not flag):
        # print("No repetition ")
        nr += 1
    else:
        r += 1

    k += 1

print(r, nr)


# l = [1, 2, 3, 4, 5, 6, 7]
l = random.sample(list(range(10000)), 100)
print(l)
sum = 0
for i in range(len(l)):
    sum += l[i]

print(sum)


# ///dot product

x = [1, 2, 4, 2]
y = [6, 4, 5, 2]


# //should have same size
# dot product i * i of both
# angle btw them
sum = 0
for i in range(len(x)):
    sum += (x[i] * y[i])
print(sum)


# add two matrices
# //matrices
# matrix addition
dim = 3
r1 = [1, 2, 3]
r2 = [4, 5, 6]
r3 = [7, 8, 9]
s1 = [1, 2, 1]
s2 = [2, 3, 3]
s3 = [5, 5, 5]
a = []
b = []
a.append(r1)
a.append(r2)
a.append(r3)
b.append(s1)
b.append(s2)
b.append(s3)

print(a)
print(b)


c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # necessary to initializing

for i in range(dim):
    for j in range(dim):
        c[i][j] = a[i][j] + b[i][j]

print(c)
# chnage it multiple more dimension


# //multiply two matrices


# / a[i][k] + b[k][j]
dim = 3
r1 = [1, 2, 3]
r2 = [4, 5, 6]
r3 = [7, 8, 9]
s1 = [1, 2, 1]
s2 = [2, 3, 3]
s3 = [5, 5, 5]
a = []
b = []
a.append(r1)
a.append(r2)
a.append(r3)
b.append(s1)
b.append(s2)
b.append(s3)

print(a)
print(b)


c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # necessary to initializing
# c ij is the dot product of ith row and jth columns
for i in range(dim):
    for j in range(dim):
        # c[i][j] =/
        for k in range(dim):
            c[i][j] = c[i][j] + (a[i][k] * b[k][j])

print(c)

# //easier way
# pip install numpy
X = numpy.mat(a)
Y = numpy.mat(b)
print(X * Y)


# //the code is for insertion srt


L = [90, 47, 8, 18, 10, 7]
S = [L[0]]  # list containing just one element
for i in range(1, len(L)):
    flag = True
    for j in range(len(S)):
        if L[i] < S[j]:
            before_j = S[: j]  # elements in S before index j
            new_j = [L[i]]		# list containing just one element
            after_j = S[j:]  # elements in S starting from index j
            # what is the size of S now?
            S = before_j + new_j + after_j
            # what is the size of S now?
            flag = False
            break
    if flag:
        S.append(L[i])
print(S)
