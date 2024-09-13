# File Name: passwordChecker.py
# Purpose:   This program asks the user to enter a password
#            and checks if it is valid or not
# Author:    Adelaida A. Medlock
# Date:      January 27, 2024

# Function to see if a password is valid or not
# A valid password must:
#   1. be at least 8 characters
#   2. contain at least one lower case letter
#   3. contain at least one upper case letter
#   4. contain at least one digit
#   5. contain at least one special character (non-letter non-digit)
# The function returns a Boolean
def isValidPassword_V1(password) :
    # check length first
    if len(password) < 8 :
        return False
    # password has 8 or more characters
    else :
        # initialize counters
        lowerChars = 0
        upperChars = 0
        digits = 0
        specialChars = 0
        
        # loop through the characters of the string
        index = 0
        while index < len(password) :
            char = password[index]
            if char >= 'A' and char <= 'Z':
                upperChars +=1
            elif char >= 'a' and char <= 'z':
                lowerChars +=1
            elif char >= '0' and char <= '9':
                digits +=1    
            else :
                specialChars +=1
            
            # increase index
            index += 1
            
        # outside the loop check if if there is at least
        # one of each: lower, upper, digit, special
        if lowerChars >= 1 and upperChars >= 1 and digits >= 1 and specialChars >= 1 :
            return True
        else :
            return False

# A second version
def isValidPassword_V2(password) :
    # check length first
    if len(password) < 8 :
        return False
    # password has 8 or more characters
    else :
        # initialize counters
        lowerChars = 0
        upperChars = 0
        digits = 0
        specialChars = 0
        
        # loop through the characters of the string
        index = 0
        while index < len(password) :
            char = password[index]
            if char.islower() :
                lowerChars += 1
            elif char.isupper() :
                upperChars += 1
            elif char.isdigit() :
                digits += 1
            elif not char.isalnum() :
                specialChars += 1
            
            # increase index
            index += 1
        
        # outside the loop check if if there is at least
        # one of each: lower, upper, digit, special
        if lowerChars >= 1 and upperChars >= 1 and digits >= 1 and specialChars >= 1 :
            return True
        else :
            return False
        
# The main script
if __name__ == "__main__":
    
    passw = input('Enter a password: ')
    if isValidPassword_V1(passw) :
        print('Your password is valid')
    else :
        print('Your password is not valid')
    

