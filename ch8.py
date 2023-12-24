#answer no 1

def maximum(num1 ,num2 ,num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3 
        
m = maximum (13,55,2)
print("the value of maximum is " + str(m))

# ANSWER NO 2

def farh (cel):
    return (cel*(9/5)) + 32

c=0
f=farh(c)
print("farenhiet temperature is " + str(f))

#ANSWER NO 3

print("hello",end=" ")
print("how",end=" ")
print("are",end=" ")
print("you?",end=" ")

# ANSWER NO 4

n=3
for i in range(n):
    print("*"*(n-i))