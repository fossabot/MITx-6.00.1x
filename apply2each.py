nums = [1,2,3,4,5]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def timesFive(a):
    return a * 5

applyToEach(nums, timesFive)

print(nums)

names = ['jose','jewell']

def getLength(x):
    return len(x)

applyToEach(names,getLength)

print(names)