#Program: MoreFunctions.py
#Purpose: Demo advanced functions features
#Author:  Adelaida Medlock
#Date:    February 24, 2024

# a void function
def madLibs() :
    '''
     Example function with no parameters and no return value
     This function simulates the mad libs game
     Sample Call: madLibs()
    '''
    noun1 = input('Enter a noun: ')
    noun2 = input('Enter a plural noun: ')
    verb1 = input('Enter a verb in present tense: ')
    verb2 = input('Enter another verb in present tense: ')
    adjective1 = input('Enter an adjective: ')
    adjective2 = input('Enter another adjective: ')
    noun3 = input('Enter a plural noun: ')
    adjective3 = input('Enter an adjective: ')
    
    print()
    print("The Magic Computers")
    print("Today, every student has a computer small enough to fit into their " + noun1 + ".")
    print("Students can solve any math problem by simply pushing the computer's little " + noun2 + ".")
    print("Computers can add, multiply, divide, and " + verb1 + ".")
    print("They can also " + verb2 + " better than a human. ", end = "")
    print("Some computers are " + adjective1 + ".")
    print("Others have a(n) " + adjective2 + " screen that shows all kinds of ", end = "")
    print(noun3 + " and " + adjective3 + " figures.")

def calculateGrade(midterm, final, labs) :
    '''
     Purpose:
      Calculate a course grade based on a weighted average
 
     Parameters:
      midterm: an integer representing the midtem exam grade
      final:   an integer representing the final exam grade
      labs:    a float representing the average of all labs
  
     Return value: the calculated grade as a float
 
     Sample Call: grade = calculateGrade(100, 85, 90.50)
    '''
    return midterm * 0.25 + final * 0.25 + labs * 0.50

# multiple return statements using conditional branching
def assignLetterGrade(score) :
    '''
     Purpose:
      Assign a letter grade based on a numeric grade
 
     Parameters:
      score: an integer representing a grade
  
     Return value: the letter grade as a string
 
     Sample Call: letter = assignLetterGrade(85)
    '''
    if score >= 90 :
        return 'A'
    elif score >= 80 :
        return 'B'
    elif score  >= 70 :
        return 'C'
    elif score >= 60 :
        return 'D'
    else :
        return 'F'

# Function that 'returns' multiple values
# returned values are packed in a list
def makeChange(pennies) :
    '''
     Purpose:
      Convert a given amount of pennies into the proper coin denominations
 
     Parameters:
      pennies: an integer representing an amount of cents
  
     Return value: a list that contains integers representing
                   quarters, dimes, nickels, and pennies
 
     Sample Call: q, d, n, p = makeChange(85)
    '''
    CENTS_PER_QUARTER = 25
    CENTS_PER_DIME = 10
    CENTS_PER_NICKEL = 5
    
    quarters = pennies // CENTS_PER_QUARTER
    pennies = pennies % CENTS_PER_QUARTER
    dimes = pennies // CENTS_PER_DIME
    pennies = pennies % CENTS_PER_DIME
    nickels = pennies // CENTS_PER_NICKEL
    pennies = pennies % CENTS_PER_NICKEL
    
    return [quarters, dimes, nickels, pennies]

# a function with default arguments
def printDate(day, month, year, style = 0):
    '''
     Purpose:
      Print a date in either U.S. or International format
 
     Parameters:
      day: an integer representing the day in a date
      month: an integer representing the month in a date
      year: an integer representing the year in a date
      style: an integer representing the style:
             0 for U.S. and 1 for International. Default value is 0
 
     Sample Calls:
      printDate(26, 2, 2024, 1)
      printDate(26, 2, 2024, 0)
      printDate(26, 2, 2024)
    '''
    if style == 0: # print date in US format
        date = str(month) + '/' + str(day) + '/' + str(year)
        print(date)
    elif style == 1: # print date in International format
        date = str(day) + '/' + str(month) + '/' + str(year)
        print(date)
    else:
        print('Invalid Style') 

# common error: putting the parameter with default value
# before parameters that require that arguments are passed
# def printDateV2(day, month, style = 0, year):
#     if style == 0: # print date in US format
#         date = str(month) + '/' + str(day) + '/' + str(year)
#         print(date)
#     elif style == 1: # print date in International format
#         date = str(day) + '/' + str(month) + '/' + str(year)
#         print(date)
#     else:
#         print('Invalid Style') 

# a second example of default arguments
def greet(name = 'stranger', message = 'good morning!'):
    '''
     Purpose:
      Print a personalized greeting
 
     Parameters:
      name: a string representing the name of a person.
            Default value is 'stranger'
      message: an string containing the greeting message.
               Default value is 'good morning!'
     
     Sample Calls:
      greet('Ollie', 'have a great day!')
      greet('Ollie')
      greet()
    '''
    print('Hello ' + name + ', ' + message)
    return
     
# another example of default arguments
def calculatePerimeter(width, height = 1):
    '''
     Purpose:
      Calculate the perimeter of a quadrilateral
 
     Parameters:
      width: a number representing the width of the quadrilateral
      height: a number representing the height of the quadrilateral
               Default value is 1
     
     Sample Calls:
      p = calculatePerimeter(10)
      p = calculatePerimeter(10, 10)
    '''
    perimeter = (2 * width) + (2 * height)
    return perimeter

# Example of a function were keyword arguments would be practical
def describePerson(firstName, lastName, age, city, occupation):
    print('First Name:', firstName)
    print('Last Name:', lastName)
    print('Age:', age)
    print('City:', city)
    print('Occupation:', occupation)

# the main script below this line
if __name__ == "__main__" :
    # test void fuction: madLibs
    madLibs()
    
    # the following variables are local to main
    # they can be accessed from point of creation
    # until the end of the main script
    finalExam = 100
    midtermExam = 75
    labAverage = 88
    labSum = 780      
    
    # calling functions that return values
    # storing the returned value in a variable for later use
    grade = calculateGrade(midtermExam, finalExam, labAverage)
    print('\nYour final grade is:', grade)

    # using the returned value in an expression
    extraCredit = 5
    grade2 = calculateGrade(midtermExam, finalExam, labAverage) + extraCredit
    print('With extra credit your final grade is:', grade2)

    # nesting function calls 
    print('Letter grade for', grade2, 'is:', assignLetterGrade(grade2))
    print()

    # calling a function that returns a list
    change = int(input('Enter the amount of change in pennies: '))
    q, d, n, p = makeChange(change)  #unpacking the list
    print(change, 'cents is equal to', q, 'quater(s),', end = ' ')
    print(d, 'dime(s),', n, 'nickel(s), and', p, 'cent(s).')
    print()

    #calling functions with default arguments
    print('Printing dates in different formats')
    printDate(26, 2, 2024)
    printDate(26, 2, 2024, 1)
    printDate(26, 2, 2024, 0)
    print()

    #calling functions with default arguments
    user = input('Enter your name: ')
    greet(user, 'how are you?')
    greet(user)
    greet()
    print()
    
    #calling functions with default arguments
    w = int(input('Enter the width: '))
    h = int(input('Enter the height: '))
    perimeter1 = calculatePerimeter(w, h)
    perimeter2 = calculatePerimeter(w)
    print('perimeter1 is', perimeter1)
    print('perimeter2 is', perimeter2)
    print()
    
    # using keyword arguments
    describePerson("Alice", "Brown", 30, city = "New York", occupation = "Engineer")
    print()
    describePerson(city = "New York", occupation = "Engineer", age = 30, firstName = "Alice", lastName = "Brown")
  
