# Program: collegepayoff.py
# Purpose: Determine how many years would be needed
#          to work at minimum wage to pay off a
#          loan for college tuition
# Authors: Mark Boady, Adelaida Medlock
# Date:    January 12, 2024

# Determine Total Tuition for College
def calculateTotalTuition(costPerTerm, numTerms):
    totalTuition = costPerTerm * numTerms
    return totalTuition

# Determine Total Cost with Loan Interest added in
def calculateTotalLoan(principal, interest, years):
    # Monthly Interest Rate
    rate = (interest / 12) / 100
    
    # Number of Months
    numberOfMonths = years * 12
    
    # Formula Numerator
    numerator = rate * ((1 + rate) ** numberOfMonths)
    
    # Formula Denominator
    denominator = ((1 + rate) ** numberOfMonths - 1)
    
    # Monthly Payment
    monthlyPayment = principal * numerator / denominator
    
    # Multiply by number of months
    totalLoan = monthlyPayment * numberOfMonths
    
    # Return Result
    return totalLoan

# Determine how many years at minimum wage
# are required to pay off total loan
def calculateYearsNeeded(amountToPay, wage):
    hours = amountToPay / wage
    weeks = hours / 40
    years = weeks / 52
    return years

# Determine and print the cost of tuition,
# the cost with interest, and how many years
# would be needed to pay off the loan if earning
# minimum wage
if __name__ == "__main__":
    # Get information from the user
    college = input("Enter the name of your University: ")
    termPrice = float(input("Enter the cost per term: "))
    numTerms = int(input("Enter the number of terms needed to graduate: "))

    # Known facts
    yearlyInterestRate = 5.50 
    minWage = 7.25
    loanTerm = 10   # in years
    
    # Process
    tuition = calculateTotalTuition(termPrice, numTerms)
    loan = calculateTotalLoan(tuition, yearlyInterestRate, loanTerm)
    years = calculateYearsNeeded(loan, minWage)
    
    # Output
    print(college, "Tuition: ${:.2f}".format(tuition))
    print(college, "Loan: ${:.2f}".format(loan))
    print("Years Needed: {:.2f}".format(years))



