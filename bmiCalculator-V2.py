
#Purpose: Simulate a BMI calculator.# Function to convert weight from pounds to Kilograms
def weightToKg(weight):
    POUNDS_PER_KG = 0.453592
    return weight * POUNDS_PER_KG

# Function to convert height from feet and inches to meters
def heightToMeters(feet, inches):
    INCHES_PER_FOOT = 12
    INCHES_PER_METER = 0.0254
    totalInches = feet * INCHES_PER_FOOT + inches
    return totalInches * INCHES_PER_METER

# Function to compute a person's BMI using the formula:
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
    
# Function to perform input validation
def validateInput(prompt, lowerBound, upperBound) :
    validData = False 
    while not validData:
        number = int(input(prompt))
        if number >= lowerBound and number <= upperBound:
            validData = True
        else :
            print("Invalid input. Please try again.")
    return number


# The main script
if __name__ == "__main__" :
    again = 'Y'
    while (again != 'N') and (again != 'n'):
        # introduction
        print("BMI Calculator")

        # Get input from user and validate it
        weight =  validateInput("Enter your weight in pounds: ", 1, 300)
        heightFeet = validateInput("Enter your height (feet): ", 1, 7)
        heightInches = validateInput("Enter your height (inches): ", 0, 11)
 
        # Calculate and display BMI
        result = calculateBMI(weight, heightFeet, heightInches)
        print("Your BMI is", round(result, 2))

        # Determine and print status of person's weight
        print("Your status is:", weightStatus(result))
        
        # ask the user if they want to stop
        print()
        again = input('Do you want to calculate another BMI? (Y/N): ')
        