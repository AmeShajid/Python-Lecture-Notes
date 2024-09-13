# Program: PriceCalculator.py
# Purpose: Calculate final price for an item.
#          Item is on sale and we need to add
#          sales taxes
# Author:  CS 171 instructors
# Date:    January 2, 2024

# declare variables to hold known values
tax =  8       # 8% sales tax
discount = 10  # item is 10% off

# get input from the user: item's price
price = float(input("Enter item's price: "))

# apply discount
deduction = price * discount / 100
price = price - deduction 

# apply sales sales tax
increase = price * tax / 100
price = price + increase

# display final price, with 2 decimal places
print("Final Price for the item:" , round(price, 2))
print("Final Price for the item: ${:.2f}".format(price))
