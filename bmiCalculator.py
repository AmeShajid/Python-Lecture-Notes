#Program: bmiCalculator.py
#Purpose: Simulate a BMI calculator. The user will enter their height 
#         (in feet and inches) and their weight (in pounds). The formula 
#         to compute the BMI given for metric units (kilograms and meters): 
#         bmi = weight / height ^ 2
#Author:  Adelaida Medlock
#Date:    January 18, 2024

# Function to convert weight from pounds to Kilograms
def weightToKg(weight):
    POUNDS_PER_KG = 0.453592
    return weight * POUNDS_PER_KG

# Function to convert height from feet and inches to meters
def heightToMeters(feet, inches):
    INCHES_PER_FOOT = 12
    INCHES_PER_METER = 0.0254
    totalInches = feet * INCHES_PER_FOOT + inches
    return totalInches * INCHES_PER_METER

# Compute a person's BMI using the formula:
# bmi = (weight in Kg) / (height in meters) ^ 2
# Assupmtion: the weight and height will be given in the English system
#             and need to be coonverted to the metric system before
#             applying the formula
def calculateBMI(weight, feet, inches):
    kilograms = weightToKg(weight)
    meters = heightToMeters(feet, inches)
    bmi = kilograms / (meters ** 2)
    return bmi

# Describe of the person's weight based on their bmi
def weightStatus(bmiValue):
    if bmiValue < 18.5:
        return "Underweight"
    elif bmiValue <= 24.9:
        return "Normal Weight"
    elif bmiValue <= 29.9:
        return "Overweight"
    else:
        return "Obese"
    
# The main script
if __name__ == "__main__" :
    # introduction
    print("BMI Calculator")

    # Get input from user and validate it
    validData = True
    weight = int(input("Enter your weight in pounds: "))
    if weight > 0 :
        heightFeet = int(input("Enter your height (feet): "))
        heightInches = int(input("Enter your height (inches): "))
        if heightFeet <= 0 or heightInches < 0 :
            print('Error: invalid value for height.')
            validData = False
    else :
        print('Error: Weight is too low.')
        validData = False
    
    # Decide if we should exit the program
    if not validData :  
        print('Invalid data. Your BMI cannot be calculated')
    else:
        # Data is valid, calculate BMI
        result = calculateBMI(weight, heightFeet, heightInches)
        print("Your BMI is", round(result, 2))

        # Determine status of person's weight
        print("Your status is:", weightStatus(result))
        
        























