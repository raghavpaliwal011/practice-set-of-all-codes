class vector:
    def __init__(self , vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str += f"{i}a{index} +"
            index +=1
        return str1
v1 = vector ([1,4,6])
print(v1)