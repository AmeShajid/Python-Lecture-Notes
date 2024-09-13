# Program: Trace-Recursion-Practice.py
# Purpose: Practice identifying base and recursive steps
#          Practice tracing recursive functions
# Author:  Adelaida Medlock
# Date:    February 16, 2024

# Exercise 1-A:
# part 1: identify base case(s) and recursive step(s)
# part 2: what does the funtion do?
def printPattern(sideLen):
    if sideLen < 1 :  
        return   
    print('[]' * sideLen)
    printPattern(sideLen - 1)  
    
# Exercise 1-B:
# part 1: identify base case(s) and recursive step(s)
# part 2: what does the funtion do?    
def printPattern2(sideLen):
    if sideLen < 1 :  
        return
    printPattern2(sideLen - 1) 
    print('[]' * sideLen)
 
# Exercise 2:
# part 1: identify base case(s) and recursive step(s)
# part 2: what does the funtion do?
def mystery(number) :
    if number <= 0 : 
        return 0
    else :
        return number + mystery(number - 1)

# Exercise 3:
# part 1: identify base case(s) and recursive step(s)
# part 2: what does the function return when the list is [1, 2, 3, 4, 5]?
# part 3: what do you think this function does?
def enigma(myList) :
    if len(myList) == 1:  
        return myList[0]
    else:
        m = enigma(myList[1:]) 
        if m > myList[0]:    
            return m
        else:
            return myList[0] 

# Exercise 4:
# part 1: identify base case(s) and recursive step(s)
# part 2: what does the funtion return when number is 20?
# part 3: what do you think this function does?
def secret(number) :
    if number <= 0 :  
        return 0
    else :
        return secret(number // 2) + 1 


print(mystery(4))
