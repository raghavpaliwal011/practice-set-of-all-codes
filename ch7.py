# ANSWER NO 1

num = int (input("enter a number"))
for i in range(1,12):
    print(f"{num}x{i}={num*i}")

# answer no 2

l1=["sohan,sachin,tanmay,raghav,deepti,mini"]

for name in l1:
    if name.startswith("s"):
        print("hello"+name)

# ANSWER NO 3

num=int(input("enter a number :"))
while i in range (1,12):
    print(f"{num}x{i}={num*i}")
    break

# ANSWER NO 4

num = int(input("enter a number : "))
prime=True
for i in range (2,num):
    if (num%i == 0 and num!=2):
        prime=False
        break
    if prime:
        print("this number is prime")
    else:
        print("this number is not prime")

# ANSWER NO 5

num =int(input("enter a number : "))
factorial = 1
for i in range (1,num+1):
    factorial = factorial*1
print(f"the factorial of {num} is {factorial}")

#aANSWER NO 6

num =int(input("enter a number : "))
factorial = 1
while i in range (1,num+1):
    factorial = factorial*1
print(f"the factorial of {num} is {factorial}")