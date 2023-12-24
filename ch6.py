#ANSWER NO 1

num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
num3=int(input("enter number 3:"))
num4=int(input("enter number 4:"))

if(num1>num2):
    f1=num1
else:
    f1=num4
if(num2>num2):
    f2=num2
else:
    f2=num2
if(f1>f2):
    print(str(f1)+"is greater")
else:
    print(str(f2)+"is greater")

#ANSWER NO 2
SUB1=int(input("enter first subject marks \n"))
SUB2=int(input("enter second subject marks \n"))
SUB3=int(input("enter third subject marks \n"))
SUB4=int(input("enter fourth subject marks \n"))

if(SUB1<33 or SUB2<33 or SUB3<33 or SUB4<33):
    print("YOU ARE FAIL")

elif(SUB1+SUB2+SUB3+SUB4)/3<40:
    print("you are fail")

else:
    ("you are passed")

#ANSWER NO 3

text=input("enter the text\n")

if("make a lot of money"in text):
    spam=True

elif("buy this too make a 1 million dollars" in text):
    spam =True

elif("no one will be richer than you once you apply this policy" in text):
    spam=True

else :
    spam=False

if(spam):
    print("this text is a spam")

else:
    print("this text is not a spam")

# ANSWER NO 4

a=("raghav is  good boy")
print(len(a))

# ANSWER NO 5

names=["kavish,devansh,krishna,yuvraj,ramashree"]
name=input("enter your name to check\n")

if name in names:
    print=("your name is present in the list")

else:
    print("your name is not present in the list")

#aur isi ke sath 6th chapter complete ab bhaiya mujhe ulta nahi latkayenge
