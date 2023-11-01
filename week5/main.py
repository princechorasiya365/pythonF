# //intro to week 5
import random


def add(a, b):
    print(a+b)


# functions
add(3, 4)


def sub(a, b):
    print(a-b)


sub(3, 4)


def discount(cost, dis):
    ans = cost - (cost) * dis/100
    print(ans)


discount(100, 8)
discount(1343434534, 0)

# add(3,4) + sub(4,3)  gives error as we dont have any retunr values


def add1(a, b):  # parameters
    return a+b


print(add1(4, 5))
ans = 10 + add1(4, 5)  # arguments
print(ans)  # we must have return value

print("Enter the cost price: ")
cost = int(input())


# more functions
# func on list
# find the min #

L = []
for i in range(100):
    L.append(random.randint(1, 10))


def minL(l):
    mini = l[0]
    for i in l:
        if (i < mini):
            mini = i
    return mini


print(minL(L))
# find the max element as well

# append before of list


def append_before(L):
    newL = []
    newL.append(23)

    newL += L
    return newL


L = append_before(L)

print(L)


# //append after  find the average of the lsit
# using functions
# modular approach to programming


# //sorting using functions
def mini(l):
    minia = l[0]
    for i in l:
        if (minia > i):
            minia = i
    return minia


def sort(L):
    # obvious sort
    # find the min append to new list remove the min from list
    l = []
    while len(L) > 0:
        m = mini(L)
        l.append(m)
        L.remove(m)
    print(l)


L = [4, 3, 5, 2]
sort(L)

# functional or modular approach to programming

# //matrix multiplication using functions

# initiate the matrix


def initC(dim):
    l = []
    for i in range(dim):
        row = []
        for j in range(dim):
            row.append(0)
        l.append(row)
    return l


def find_dot(u, v):

    ans = 0
    for i in range(len(u)):

        ans += (u[i] * v[i])
    return ans


def row(M, dim, i):
    l = []
    for k in range(dim):
        l.append(M[i][k])
    return l


def col(M, dim, j):
    l = []
    for k in range(dim):
        l.append(M[k][j])
    return l


def mat(A, B, dim):
    C = initC(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j] = find_dot(row(A, dim, i), col(B, dim, j))

    return C


a = [[1, 2], [3, 4]]
b = [[2, 3], [4, 5]]
print(mat(a, b, 2))


# recursion
# theory
# compound interest
# fn = 2000 * (1.1) **n
# other way around
# fn = fn-1 *(1.1)

# sum(n) = sum(n-1) +n
# fact(n) = n * fact(n-1)

# //recursion
# fund the sum of n numbers
def sumn(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def sumr(n):
    if (n == 0):
        return 0
    return n + sumr(n-1)


print(sumr(10))


def cir(p, n):
    if (n == 0):
        return p
    return 1.1 * cir(p, n-1)


print(cir(2000, 100))


def fact(n):
    if (n == 0):
        return 1
    return n * fact(n-1)


print(fact(1))
# type of function arguments
# positional
# keyword arguments
# default arguments
# default arguments only after u have finished all the postional arguments

# return value of functions is none

# scope of variables


def myfunction(x):
    global x
    # tell teh interpreter to look fro global var
    x = x ** 2
    return x


x = 5
print(x)
print(myfunction(x))  # local and global
print(x)

# call by value  passing a copy of the variable
# and scope of the value scope is local to the function


# type of functions
# //builtin print input len
# library function log sqrt calendar month()
# class function upper lower strip count
# user defined
