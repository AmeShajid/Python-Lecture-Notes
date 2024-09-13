#Program: SearchingAlgorithms.py
#Purpose: Demo Linear and Binary Search Algorithms
#Author:  Adelaida Medlock
#Date:    February 24, 2024

# imports needed 
import time
import random

# Linear Search: using a for loop
def linearSearch(values, key):
    for index in range(len(values)):
        if values[index] == key:  # found, return location of key
            return index
    return -1   # not found

# Linear Search: second version, using a while loop
def linearSearch_V2 (values, key) :
    found = False
    index = 0
    foundIndex = -1 
    while (found == False and index < len(values)) :
        if values[index] == key :
            found = True 
            foundIndex = index 
        else :
            index = index + 1 
    return foundIndex


# Binary Search - loop version
def binarySearch(values, key):
    start = 0
    end = len(values) - 1

    while end >= start:
        mid = (start + end) // 2  # get the index of the middle value
        if values[mid] < key:   # search on the right
            start = mid + 1
        elif values[mid] > key: # search on the left
            end = mid - 1
        else:  # found
            return mid
    
    return -1 # not found

# Binary Search - recursion version
def binarySearch_V2(values, start, end, key) :
    if start > end :   # not found
        return -1
   
    mid = (start + end) // 2  # index of middle value
    
    if  values[mid] == key : # found
        return mid
    
    elif values[mid] < key : # key is in the upper half (or right side)
        return binarySearch_V2(values, mid + 1, end, key)
    
    else : # key is in the lower half (or left side)
        return binarySearch_V2(values, start, mid - 1, key)


def populateList():
    values = []
    for i in range(100000) :
        number = random.randint(-15000, 15000)
        values.append(number)
    return values
        
        
# main script
if __name__ == "__main__" :
    # create a list with 100K random integers
    myList = populateList()
    
    # linear search
    print('Testing linear search')
    key = int(input('Enter a value to search: '))
    
    # set timer and search for item
    startTime = time.time()
    index = linearSearch(myList, key)
    endTime = time.time()
    
    # display results
    if index != -1 :
        print(key, 'was found at index', index)
    else :
        print(key, 'was not found in the list')

    print('Time taken for linear search:', (endTime - startTime), 'seconds') 
    
    # binary search
    print('\nTesting binary search')
    key = int(input('Enter a value to search: '))
    
    # list must be sorted first
    myList.sort()
    
    # set timer and search for item
    startTime = time.time()
    index = binarySearch_V2(myList, 0, len(myList) - 1, key)
    endTime = time.time()
    
    # display results
    if index != -1 :
        print(key, 'was found at index', index)
    else :
        print(key, 'was not found in the list')
    
    print('Time taken for binary search:', (endTime - startTime), 'seconds')
    