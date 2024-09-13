#Program: SortingAlgorithms.py
#Purpose: Implement Insertion and Quick Sorts
#Author:  Adelaida Medlock
#Date:    February 25, 2024

'''
Purpose:      Exchange the values of two elements in a list
Parameters:   a list of values,
              the indeces of the elements to be swapped
Return value: none
Sample call:  swap (myList, 3 ,5)
'''
def swap(values, i, j):
    temp = values[i]
    values[i] = values[j]
    values[j] = temp

'''
Purpose:      Implement the insertion sort algorithm
              This implementation sorts values in ascending order
Parameters:   a list of items to be sorted
Return value: none. Values are sorted in place.
Sample Call:  insertion_sort(myList)
'''
def insertionSort(values):
    for i in range(1, len(values)):
        j = i
        # Insert values[i] into sorted part 
        # stopping once values[i] in correct position
        while j > 0 and values[j] < values[j - 1]:
            # Swap values[j] and values[j - 1]
            swap(values, j, j - 1)
            j = j - 1

'''
Purpose:      partition a list into two parts:
              one with the high values and
              one with the low values
Parameters:   a list of values
              the index of the 1st element
              the index of the last element
Return value: an integer representing the index to be used 
              as the partition point
Sample Call:  splitPoint = partition(myList, 0, len(myList) - 1)
'''
def partition(values, fromIndex, toIndex):
    # Pick middle element as pivot 
    midpoint = fromIndex + (toIndex - fromIndex) // 2
    pivot = values[midpoint]

    # Initialize variables
    done = False
    leftIndex = fromIndex
    rightIndex = toIndex
    while not done:
        # Increment leftIndex while values[leftIndex] < pivot 
        while values[leftIndex] < pivot:
            leftIndex = leftIndex + 1
        
        # Decrement rightIndex while pivot < values[rightIndex] 
        while pivot < values[rightIndex]:
            rightIndex = rightIndex - 1
        
        # If there are zero or one items remaining,
        # all numbers are partitioned. Return rightIndex 
        if leftIndex >= rightIndex:
            done = True
        else:
            # Swap values[leftIndex] and values[rightIndex],
            # update leftIndex and rightIndex
            swap(values, leftIndex, rightIndex)
            leftIndex = leftIndex + 1
            rightIndex = rightIndex - 1
    
    return rightIndex

'''
Purpose:      Implement the quick sort algorithm, using recursion
              This implementation sorts values in ascending order
Parameters:   a list of values
              the index of the 1st element
              the index of the last element
Return value: none. Values are sorted in place.
Sample Call:  quick_sort(myList, 0, len(myList) - 1))
'''
def quickSort(values, fromIndex, toIndex):
    # Base case:
    # If there are 1 or zero values to sort, there is nothing to sort
    if fromIndex < toIndex:
        # Partition the data within the list. Value splitPoint returned
        # from partitioning is the location of last item in low partition
        splitPoint = partition(values, fromIndex, toIndex)
    
        # Recursively sort low partition (fromIndex to splitPoint) and
        # high partition (splitPoint + 1 to toIndex) 
        quickSort(values, fromIndex, splitPoint)
        quickSort(values, splitPoint + 1, toIndex)
