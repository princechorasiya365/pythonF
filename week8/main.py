#//intro to recursion 
# file handling 
# do something about element and leave the rest to other 
# //check if a given list has a zero

def checkHas(l):
    if(len(l)==0):
        return False
    if(l[0]==0):
        return True
    else:
        return checkHas(l[1:])
#not a efficent code why 
l = [4,5,23,42,0]
print(checkHas(l))

# iterative is better

#sort recursively
# //recursively sort the llist  
def minia(l):
    mini = l[0]
    for x in l:
        if(x<mini):
            mini = x
    return mini

def sort(l):
    if(len(l)<=1):
        return l
        
    m = minia(l)
    # //recursively sort the llist 
    l.remove(m)
    return ([m] + sort(l))

	
              

# finds the mini


l =[4,3,2,5,9]
l=sort(l) #noto storing the result 
print(l)
def ls(l,val):
  for i in l:
    if(val==i):
      return True
  
  return False


l =[1,2,3,4,5,6,7,8,9,10]
l =list(range(100))
print(ls(l,11))

import time 
def sum(n):

  sum =0
  a = time.time()
  for i in range(n):
    sum += i
  b =time.time()
  print("execution time",b-a)
  return sum


sum(10 ** 9)

# // opoerator for the integral part 
 
#  and (begin + end )//2 gives us the mid of the array /

# concpet of time complexity 


#binary search implementaion
import time  
def binary_Search(l,k):
  "alternatie for linear serch in efficent way "

  
  begin =0
  end =len(l)-1
  if(len(l)==0):
    return -1
  

  while(begin < end):
    mid = (begin+end)//2
    if l[mid] >k :
      end = mid -1
    elif l[mid] <k:
      begin = mid+1
    else:
      
      return 1
  if(l[begin]==k or l[end]==k):
    return 1
  return -1


# binary search works on sorted lsit 
l =list(range(0))
print(l)
a = time.time()
print(binary_Search(l,1))
b =time.time()
print("E:",b-a) 

# //recursive bianry search 
import time 

#recursive binary search:

def rbs(l,k):
  begin =0
  end = len(l)
  if(len(l)==0):
    return -1
  mid =(begin + end)//2
  if(l[mid]==k):
    return 1
  elif (l[mid] <k):
    return rbs(l[mid+1 : end],k)
  else:
    return rbs(l[begin:mid-1],k)
  
l =list(range(10000000))
# print(l)
a = time.time()
print(rbs(l,-1))
b =time.time()

print("T:",b-a)


#wrtie the iterative first 
d ={'Jahangir': 'Akbar', 'Akbar': 'Humayun', 'Humayun': 'Babur'}
present ='Jahangir'
past='Babur'

# d = {'Anil': 'Krishna', 'Mohan': 'Prasanna', 'Krishna': 'Prasanna', 'Prasanna': 'Mukesh'}
# present ='Anil'
# past ='Prasanna'
def ancestry(d,present,past):
  l =[]
  keys = d.keys()
  l.append(present)
  while(past != present):
    if(present in keys):
      l.append(d[present])
      present = d[present]
  
  return l

print(ancestry(d,present,past)) 

#convert to recursive
def ra(d,present,past):
  if(present==past):
    return [past]
  l =[]
  l.append(present)
  present = d[present]
  return l + ra(d,present,past)


print(ra(d,present,past))