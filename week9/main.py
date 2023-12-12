#file handling  asn pandas big files 

# kitchen store more frequently used things ram
# storage keep the rest there and files

# fast storage ram /volatile 
# slow storage  hard disk  xternal memory //non volatile 
# ram is fast but slow and limited 

# mp3 files in hard disk 

# find a number in a list 
# how to handle file using python 
# //readin and wiritng to a fiel 

f =open("./week9/my_file.txt","w")
f.write("prince") #return the no letters written 
f.write("IITM ")
f.write("India ")
f.close()

f =open("./week9/my_file.txt","r")
s = f.read()
print(s)

#write and read 

# big text file handling 


#writes 100 lines randomly 

# lecture 3 
import random 

f =open("file.txt","a")
for i in range(10):
  for i in range(100000): #crashes after 10^8 
    f.write(str(random.randint(1000000000,10000000000-1)))
    f.write("\n") 

f =open("file.txt","r")
# c =f.readline() #reads 1 line
c='0'
flag =0
# print(c)
num =8935507536
#eof files line   convert null into int we get error 
while(c!=''): #EOF 
  c=f.readline() #converting takes care of the trailing '\n'n =
  if(c==''):
    break
  n =int(c)
  
  if(n==num):
    print("found number")
    flag =1
    break

if(not flag):
  print("Number not found")



# //encryption 
# //ceaser cipher 
# take a input file encrypt it using ceaser cipher 3 unit 

import string 
f =open("file.txt","w")
f.write("mynameisprince")
f.close()

f =open("file.txt","r")

l =list(string.ascii_lowercase)
# print(l)

# //create the dict
d={}
for i in range(len(l)):
  d[l[i]] = l[(i+3)%26]
print(d)
g =open("encrypted.txt","w")

c =f.read(1)
while(c!=''):
  g.write(d[c])
  c=f.read(1)

f.close()
g.close()

# decryption wrtie the code 

f =open("file.txt","r")
f.seek(4) #go forward or backward  moves linearly as to the place 

# actg human genes 
f.read() #//read the whole 
# finding  subsequecne in string 

# knuth mp //alogorithm to find subseuqence in a large file 


# //why pandas 

import pandas
# pandas.s 
# various uses of pandas  e

import pandas as pd 
score = pd.read_csv("file.txt")
# score. //various functios releated tto pandas 

import pandas as pd 
score = pd.read_csv("file.txt")
# score. //various functios releated tto pandas 

print(score) 
#store the variable as tabular daata also called data frame 
type(score) #typr of the table is data frame 2d
# any columns is called series 
type(score['marks']) #series 1 d

score.head() #print first five rows by deault 
score.tail() #index from end 
score['column_name'] #prints the column 

print(score['name'] =='nisha') #prints the details of the student having name nisha 

# data can be read coulmn wise as well as row wise 

# find marks of topper boys and topper girl 

print(score[score['Name']]=='M') 
print(score[score['Gender']=='M']['total'])
print(score[score['Gender']=='M']['total'].max())

# //dividng teh students into four categories 
print(score[score['Physics'] >85].shape[0]) #shape has tuple (0,1) give the students here 
print(score[score['Physics'].between(70,80)])
print(score[score['Physics'].between(60,70)])
print(score[score['Physics']<60])


# //find the student above 85 and female 
print(score[score['Physics'] >85 & score['Gender']=='M'].shape[0])
# pandas has its own operators 

subject  = ['Mathematics','Physics','Chemistry']

for sub in subject:
  print("above 85 in ",sub)
  avg =score[sub].mean()
  #prints the score of all students above average 
  print(score[score['Physics'] >avg & score['Gender']=='M'].shape[0])
  print(score[score['Physics'] >avg & score['Gender']=='F'].shape[0])
  print(score[score['physics']>avg].groupby('gender').groups)


# //student above below average 

# group by 
print(score.groupby('Gender').groups) #prints a list of card number where gender is female and male makes a bucket 

# useful when bining 


def do_something(filename):
    f = open(filename, 'r')
    maxword = f.readline().strip()
    count = 1
    # we are now at the beginning of the second line
    for line in f:
        word = line.strip()
        if len(word) > len(maxword):
            maxword = word
            count = 1
        elif len(word) == len(maxword):
            count += 1
    
    f.close()
    return count

print(do_something('words.txt'))


def do_something(infile, gender, outfile):
    f = open(infile, 'r')
    g = open(outfile, 'w')
    header = f.readline()
    # we are now at the beginning of the second line of the file
    # 'good,M,great'.replace(',M,', ',')
    # returns 'good,great'
    header = header.replace(',Gender,', ',')
    g.write(header)
    
    for line in f.readlines():
        fields = line.strip().split(',')
        gender_in_file = fields[2]
        if gender_in_file == gender:
            out_line = line.replace(f',{gender},', ',')
            g.write(out_line)
    
    f.close()
    g.close()
    
do_something('scores.csv', 'F', 'out.csv')

def do_something(infile, gender, outfile):
    f = open(infile, 'r')
    g = open(outfile, 'w')
    header = f.readline()
    # we are now at the beginning of the second line of the file
    # 'good,M,great'.replace(',M,', ',')
    # returns 'good,great'
    header = header.replace(',Gender,', ',')
    g.write(header)
    
    for line in f.readlines():
        fields = line.strip().split(',')
        gender_in_file = fields[2]
        if gender_in_file == gender:
            out_line = line.replace(f',{gender},', ',')
            g.write(out_line)
    
    f.close()
    g.close()
    
do_something('scores.csv', 'F', 'out.csv')