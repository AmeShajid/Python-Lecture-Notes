# Program: RecursionExamples.py
# Purpose: Practice writting recursive functions 
# Author:  Adelaida Medlock
# Date:    February 16, 2024

'''
Purpose:
    calculate the sum of all the digits in an integer number
Parameter:
    an integer number
Return Value:
    the sum of all the digits in the number passed to the function 
Sample call:
    total = sumOfDigits(12456)
'''
def sumOfDigits(number) : 
    if  number < 0 :   #take care of negative numbers
        return (-sumOfDigits( -number ) )
    if number < 10 :  #base case: a single digit number
        return number
    else:
        # recursive call
        # Add the last digit to the result of summing the remaining digits
        return ( number % 10 + sumOfDigits( number // 10 ) )  

'''
Purpose:
    calculate the factorial of a number
Parameter:
    a positive integer number
Return Value:
    the result of 1 * 2 * 3 * 4 * ..... * number
Sample call:
    result = factorial(2)
'''
def factorial (number) :
    if (number == 0):  # Base case
        return 1 
    else :  # Recursive call
        return (number * factorial(number - 1) )

'''
Prupose:
    display a given message a certain number of times
Parameters:
    an integer that represents the number of times to display the message
    a string that represents the message to be displayed 
Return value:
    this function does not return anything
Sample Call:
    print_message(5, 'Python is fun!')
'''
# base case: times == 0 
# In this example the base case is implicit
# recursive call: print_message(times - 1, msg)
def print_message(times, message):
    if times > 0:
        print(message)
        print_message(times - 1, message) # Recursive call

'''
Purpose:
    calculate the sum of values in a numeric list
Parameters:
    a list of numeric values
    the index of the first item
    the index of the last item
Return value:
    the total of adding all values in the list
Sample Call:
    total = sumList(numList, 0, 10)
'''
# base case: when we have no more elements left in the list: start > end
# recursive step: add the first element of the list plus the resut of adding 
# the rest of elements in the list: sumList (numList, start + 1, end)
def sumList(numList, start, end):
    if start > end :  #base case: we don't have elements left in the list
        return 0
    else :
        return numList[start] + sumList(numList, start + 1, end)

'''
Second version that takes advantage of slicing
This version only takes one parameter: the list of values
'''
# base case: no elements left in my list, empty list: len < 1
# recursive step: to make the list smaller, use slicing numList[1:]
def sumList2(numList):
    if len(numList) < 1 :
        return 0
    else :
        return numList[0] + sumList2(numList[1:])

'''
Purpose:
    display a string in a interesting shape
Parameter:
    a string that represents the message to be displayed 
Return value:
    this function does not return anything
Sample Call:
    down_up_word('Python')
Sample Output:
    Python
    ython
    thon
    hon
    on
    n
    on
    hon
    thon
    ython
    Python
'''
# base case is implicit: keep going if we have at more than one character
# recursive call: make the string smaller by removing the 1st character
def down_up_word(word) :
    print (word)
    if len(word) != 1 :  #the base case is when len(word) == 1 (implicit)
        down_up_word(word[1:]) #recursive case
        print(word)

# the main script: to test our recursive functions
if __name__ == "__main__":
    pass