f = open ('poem.txt')
t = f.read
if 'twinkle' in t:
    print ("tinkle is present in poem .txt")

else:
    print ("twinkle is not present in poem.txt")
f.close()