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