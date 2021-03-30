import random

def print2DArray(x):
    for i in x:
        temp = str()
        for j in i:
            temp += str(j) + " "
        print(temp)

def findSum(x):
    sum = 0

    for i in x:
        for j in i:
            sum += j

    print(sum)

x = []
for i in range(10):
    temp = []
    for j in range(10):
        temp.append(random.randrange(0,10))
    x.append(temp)

print2DArray(x)

findSum(x)