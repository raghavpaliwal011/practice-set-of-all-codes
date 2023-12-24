#chapter 2,chater 1 was done but file is missing but practice set is there on the desktop

a=23
b=32

# 1 arithematic operators

print ("the values of 3+4 is",3+4)
print ("the values of 3*4 is",3*4)
print ("the values of 3/4 is",3/4)
print ("the values of 3-4 is",3-4)


# 2 assigment operators

a = 23
a +=23 #same goes with +,-,/,* and so on 
print(a) # writing this line is iportant so please write this while using assignment operators


# 2 assigment operators

 # writing this line is iportant so please write this while using assignment operators



# 3 comparison operators 

a=(4>7)
print(a)

#logical operators

bool1=True
bool2=False

print("the value of bool1 and bool2 is ",(bool1 and bool2))
print("the value of bool1 or bool2 is ",(bool1 or bool2))
print("the value of bool1 not bool2 is ", (not bool2))

#type casting

a="2345"
a=int(a)
print(type(a))
print(a+5)
#input function

a=input("enter a number:") 
a=str(a)
print(type(a))

#chapter 3 

#strings

greeting="good morning , "
name="raghav"
c = greeting + name
print(c)

#concatenating two strings


name="raghav"
print(name[-2])

name="raghav"
print(name[0:]) # is same as 0:1 0:2 0:3 etc

a="34"
a=int(a)
print(type(a))

#print("once upon a time there was a boy named raghav who was the most handsome boy in the world")
story="i am the most handsome boy in the world" #this is just for test
print(len(story))#it is used to find the number of a perticular character used in a perticular sentence 
print(story.endswith("d")) #it is used to find that the end letter of a story is true or false
print(story.count("d"))#it is used to count the number of a perticular letter used in a perticular sentence
print(story.count("handsome"))#it is used to count the number of a perticular word in in a perticular sentence 
print(story.capitalize())#it converts the first letter of a sentence in a capital letter(if not done)automatically
print(story.find("handsome"))#it finds that on which number that character is
print(story.replace("handsome", "the god of minecraft"))#it replaces a word or a letter

a=("Raghav is good.\n He is very good")
print(a)

#chapter 4

#list

#create a list using []
#print the list using print function
#access using a[0] a[1] a[2] etc
#chnge the value of list using
#we can create the list using the items of different types
a=[1,2,3,4,5,6]
a[0]= 23
print(a)
c=(34,"34",False,6.5)
print(c)

#list slicing
friends=["yuvraj","kavish","ramashree","himank"]
print(friends[0:4])

l1=[1,23,7,34,33]
l1.sort() #this command sorts a perticular program
print(l1)

l1=[1,23,7,34,33]
l1.reverse() #this  command reverses a perticular program
print(l1)

l1=[23,45,44,1]
l1.append(34) #adds a number at the end of a list
print(l1)

l1=[34,67,11,34]
l1.insert(0,34) #adds a perticular number at a given place in te program
print(l1)

l1=[23,56,11,99]
l1.pop(2) #removes a perticular number from program
print(l1)

l1=[34,11.23,56]
l1.remove(34) #this also removes a pertiuar number from program
print(l1)

#tuple

#we cannot update the vlues of  tuple

t=[23,34,11,12]
print(t[0])
t[3]=33

#t=() #empty tuple
#t=(1) #wrong way to declare a tuple
#t=(1,) #right way to declare a tuple

t=(1,2,3,44,66)
print(t.count(1)) #counts a perticular number in a program like how many times it is occuring in  program

t=(1,23,11,77)
print(t.index(23)) #tells on which index number that perticular number is

#chapter 5

#1 dictionary methods

mydict={
"fast":"in a quick manner",
"good":"obidient",
1:4}
print(mydict['fast'])


print(list(mydict.keys()))#pints the keys of the dictionary
print(mydict.values())#pints the values of the dictionary'
print(mydict.items())#pints the items of the dictionary'
print(mydict)
updatedict={
"yuvraj":"friend",
"ramashree":"friend"}

mydict.update(updatedict)#updates the dictionary by adding key value pairs from updatedict
print(mydict)

#diffrence between mydict.get andonly mydict command

#print(mydict.get("ramashree 2"))#returns none as ramashree2 is not present in the dictionary
#print(mydict["ramashree2"])#throw an error as ramashree2 is not present in the dictionary

print(mydict.get("ramashree"))#prints value associated with key "ramashree"
print(mydict["ramashree"])#prints value associated with key "ramashree"

#sets methods in python

a={1,2,3,4,1}
print(type(a))

# IMPORTANT:this syntax will create an empty dictionary not an empty set 

a={}
print(type(a))

# an empty set can be created using the below syntax

b=set()
print(type(b))
#this can add values to a empty set
b.add(4)#NOTE=set is a value of non repetative values andwe cannot add lists or dictionaries to set
print(b)
print(len(b)) #prints the length of the progam
b.remove(4)
print(b)

#chapter 6

a=45
if(a>3):
    print("the value of a is greaterthan 3")

elif(a>7):
    print("the value of a is greater than 7")

else:
    print("the value of a is not greater than 3 or 7")

age=int(input("Enter your age : "))
if age>18:
    print("YES")
else:
    print("NO")

# == -> equal
# >= ->greater than or equal to

age=56
if(a>33 or age<65):
    print("You can work with us")

else:
    print("You cannot work with us")

a=None
if (a is None):
    print("Yes")
else:
    print("no")

#CHAPTER NO 7

# 1 WHILE LOOP

i=0
while i<10:
    print("yes" + str(i))
    i=i+1

print("done")

#quick quiz no 1 (while loops)

i=0
while i<=50:
    print("number"+str(i))
    i=i+1

print("done")


fruits=["banana","apple","mango","watermelon"]
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1

print("done")

# FOR LOOP

fruits=["banana","apple","mango","watermelon"]
i=0
for items in fruits:
    print(items)

print("done")

# RANGE FUNCTION IN PYTHON

for i in range (1,8):  # note : if a number is writen in the first place where 1 is written the program will start with that number and end at the place where 8 is written if there is nonumber in the first place it will start from 0
    print(i)

#for loop with else

for i in range (10):
    print(i)
else:
    print("this is inside else of for")

#Breaks steatement

for i in range (10): #it breaks the statement
    print(i)
    if i==5:
         break
    
#continue statement

for i in range (10): #it continues the statement nd skip the give number
    print(i)
    if i==5:
         continue
    print(i)

#pass statement

i=4 # pass is a null statement meaning it instructs to do nothing and it can be used with oth isf or else 
if i>0:
    pass
print("raghav is a good boy")

# CHAPTER NO 8

marks1=[45,23,89,100,0]
persentage1=[sum (marks1) / 400]*100

marks2=[34,90,22,12]
persentage2=[sum (marks2) / 400]
print(persentage1 , persentage2)

def greet(name):
    print("good day"+ name)
    
greet("raghav")

def mysum(num1,num2):
    return num1 + num2
greet("raghav")
s=mysum(6,32)
print(s)

def greet(name):
    print("good day ,"+ name)

greet("raghav")

n=2
product=1
for i in range (n):
    product=product * (i+1)
print(product)

def factorial_iter(n):
    product=1
    for i in range (n):
        product=product * (i+1)
    return product

def factorial_recursive(n):
    if n == 1 or n==0:
        return 1
    return n*factorial_recursive(n-1)

f=factorial_iter(5)
print(f)

#chapter 9 i have did it but its no showing i dont know how  >:
#practice set of chapter 9 also not showing

#chapter 10

class number :
    def sum(self):
        return self.a+self.b
    
num=number()
num.a=12
num.b=34
sum=num.sum()
print(s)

'''
PascalCase
EmployeeName -->PascalCase

camelcase
is numeric, isFloatorInt-->
'''


# APPLICATION IN PYTHON
class railwayform :
    FormType = "railwayform"
    def printdata (self):
        print(f"name is {self.name}")
        print(f"name is {self.train}")

raghavsapplication=railwayform()
raghavsapplication.name="raghav"
raghavsapplication.train="mr ghochu tain"
raghavsapplication.printdata()

#SASTA GTA VICE CITY IN PYTHON

#class remote():
#    pass
#
#class player:
#    def moveright(self):
#        pass
#
#    def moveleft(self):
#        pass
#
#    def movetop(self):
#        pass
#
#remote1 = remote()
#player1 = player()
#if(remote1.isleftpressed()):
#    player.moveleft()

class employee:
    company = "google"


raghav=employee()
tanmay=employee()
deepti=employee()
mini=employee()
raghav.salary=10000
tanmay.salary=10000
deepti.salary=10000
mini.salary=10000
print (raghav.company)
print (tanmay.company)
print (deepti.company)
print (mini.company)
employee.company = "space scientist"
print (raghav.company)
print (tanmay.company)
print (deepti.company)
print (mini.company)

#instance class attributes

class employee:
    company = "google"
    salary=100

raghav=employee()
tanmay=employee()
deepti=employee()
mini=employee()

# creating instance attributes salary for four of the objects
#if we dont have a salary or any number in any number in variable it will automatically print the default value

# raghav.salary=10000
# tanmay.salary=10000
# deepti.salary=10000
# mini.salary=10000
print(raghav.salary)
print(tanmay.salary)
print(deepti.salary)
print(mini.salary)
#below line throws an error as mini.address is not present in the proggram
# print(mini.address)
#self ki practice

#chapter 9
