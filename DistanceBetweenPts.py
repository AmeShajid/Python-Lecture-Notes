#Program:     DistanceBetweenPts.py
#Purpose:     Given to points at coordinates (x1, y2) and (x2, y2), 
#             this program calculates the distance between the points
#Author:      Adelaida Medlock
#Date:        January 12, 2024

# import the math module
import math

# define function
def calculateDistance(x1, y1, x2, y2) :
    term1 = math.pow(x2 - x1, 2.0)
    term2 = math.pow(y2 - y1, 2.0)
    distance = math.sqrt(term1 + term2)
    return distance

# main script
if __name__ == "__main__" :
    # intro: information to the user
    print ('Calculating the distance between two points')

    # get data from the user
    x1 = int(input('Enter point 1, x coordinate: '))
    y1 = int(input('Enter point 1, y coordinate: '))         
    x2 = int(input('Enter point 2, x coordinate: '))
    y2 = int(input('Enter point 2, y coordinate: '))

    # calculate the distance between two points using our function
    dist = calculateDistance(x1, y1, x2, y2)

    #display the results
    print('The distance between (', x1, ',' , y1, ')', end = ' ')
    print('and (', x2, ',' , y2, ') is:', dist)