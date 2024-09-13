def sayHi():
    print("Hello!")
    return
def doubleReturn(x):
    return [x**2, x**3]
def loopy(x):
    while True:
        print(x)
        if x**2 > 100:
            return
        x+=1
Q = sayHi()
print(Q)
a,b = doubleReturn(7)
print(a)
print(b)
loopy(1)
print("*"*10)
def whatever(a=7,b=9):
    return a * b
print(whatever(1,2))
print(whatever(2))
print(whatever())
print(whatever(b=3))
print("Hi","Low",end="!\n",sep="_")
print("*"*10)

def scopey():
    y = 8
    print(a,y)
    #End of the function y is deleted!
a=3
scopey()
print(a)
#print(y)

print("*"*10)
print("Mutable")

def changeInt(a):#Immutable!
    a=a+7
    print("In Function",a)
def changeList(myList):#mutable
    '''
    This function shows a mutable
    list
    '''
    myList.append(7)
b = 9
changeInt(b)
print(b)
q = [1,2,3]
changeList(q)
print(q)



