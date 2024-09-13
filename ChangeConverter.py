# Program:  ChangeConverter.py
# Purpose:  This program asks the user for two amounts of money. Then it 
#           calculates the difference and instructs how to make change.
# Author:   Adelaida Medlock
# Date:     January 13, 2024

if __name__ == "__main__":
    # Introduction
    print('Compute the change due after paying for an item')
    print('')

    # Get Input From the User
    amountPaid = float(input("Enter Amount Paid (10.00): "))
    amountDue = float(input("Enter Amount Due (9.99): "))

    # Constants need for conversion
    CENTS_PER_DOLLAR = 100
    CENTS_PER_QUARTER = 25
    CENTS_PER_DIME = 10
    CENTS_PER_NICKEL = 5

    # First convert the amount paid and the amount due to cents
    amountPaid = int(amountPaid * 100)
    amountDue = int(amountDue*  100)

    # Computer the difference in cents. That is the chane due.
    change = amountPaid - amountDue

    # Calculate how many dollars
    dollars = change // CENTS_PER_DOLLAR
    change = change % CENTS_PER_DOLLAR

    # Calculate how many quarters
    quarters = change // CENTS_PER_QUARTER
    change = change % CENTS_PER_QUARTER

    # Calculate how many dimes
    dimes = change // CENTS_PER_DIME
    change = change % CENTS_PER_DIME

    # Calculate how many nickels and pennies
    nickels = change // CENTS_PER_NICKEL
    pennies = change % CENTS_PER_NICKEL

    #Output to the User
    print("Dollars Change:", dollars)
    print("Quarters Change:", quarters)
    print("Dimes Change:", dimes)
    print("Nickles Change:", nickels)
    print("Pennies Change:", pennies)











