#Program: GradeBook.py
#Purpose: Simulate a gradebook.
#Author:  Adelaida Medlock
#Date:    February 1, 2024

# Function to validate input from the user
# expected input must be an integer value
# between lowerBound and upperBound
def validateInput(prompt, lowerBound, upperBound) :
    validData = False 
    while not validData:
        number = input(prompt)
        if number.isdigit() :
            number = int(number)
            if number >= lowerBound and number <= upperBound:
                validData = True
        else :
            print("Invalid input. Please try again.")
    return number


# Function to find maximum grade
def findMax(grades) :
    # start by assuming first value is the maximum
    maximum = grades[0]
    
    # iterate through the list to see if we find a larger value
    for index in range(len(grades)) : 
        if grades[index] > maximum:
            maximum = grades[index]
    
    return maximum
    

# Function to find minimum grade
def findMin(grades) :
    # start by assuming first value is the minimum
    minimum = grades[0]
    
    # iterate through the list to see if we find a smaller value
    for index in range(len(grades)) : 
        if grades[index] < minimum:
            minimum = grades[index]
    
    return minimum


# Function to calculate the average
def calculateAverage(grades) :
    count = 0
    total = 0
    
    # iterate over list to count and add all the values
    for index in range(len(grades)) : 
        total = total + grades[index]
        count += 1
    
    # calculate and return averate
    average = total / count
    return average

# Function to find the median of the values.
# The median of a group of values is located in the middle of
# the list if the list's length is odd. Otherwise, the median
# is the average of the middle two values.
# Note: Values must be sorted first
def findMedian(grades):
    grades.sort()
    length = len(grades)

    if length % 2 == 0:  #even length
       median = (grades[length // 2] + grades[(length // 2) - 1]) / 2.0 
    else:  #odd length
       median = grades[length // 2]

    return median


# Function to count the number of As, Bs, Cs, Ds and Fs 
def countLetters(grades):
    # our list will store:
    # [As count, Bs count, Cs count, Ds count, Fs count]
    letterCount = [0, 0, 0, 0, 0]
    
    for grade in grades :
        if grade >= 90 :  
            letterCount[0] += 1 # As
        elif grade >= 80 :
            letterCount[1] += 1 # Bs
        elif grade >= 70 :
            letterCount[2] += 1 # Cs    
        elif grade >= 60 :
            letterCount[3] += 1 # Ds
        else :
            letterCount[4] += 1 # Fs
    
    return letterCount

 
# Function to display a report with basic stats on a list of grades 
def reportResults(stats, letterCount):
    print('You entered', stats[0], 'grades')
    print('The maximum grade is', stats[1])
    print('The minimum grade is', stats[2])
    print('The average grade is %.2f' %(stats[3]))
    print('The median grade is %.2f' %(stats[4]))
    print()
    
    print('Letter Count')
    letters = ['As', 'Bs', 'Cs', 'Ds', 'Fs']
    for index in range(len(letters)):
        print('%d %s'%(letterCount[index], letters[index]))
    

# the main script
if __name__ == "__main__":
    # ask user how many grades they will enter
    numberOfGrades = validateInput('How many grades do you want to enter? ', 1, 1000)
    
    # get and validate grades. Valid values are appended to grades list
    grades = []
    for count in range(0, numberOfGrades) :
        grade = validateInput('Enter a grade between 0 and 100: ', 0, 100)
        grades.append(grade)

    # get maximum and minimun grades
    maxGrade = findMax(grades)
    minGrade = findMin(grades)
    
    # get average and median
    average = calculateAverage(grades)
    median = findMedian(grades)
    
    # get letter grades distribution
    gradeDistribution = countLetters(grades)
    
    # set up stats list to send to reporting function
    stats = [numberOfGrades, maxGrade, minGrade, average, median]
    
    # display results
    print()
    reportResults(stats, gradeDistribution)
    