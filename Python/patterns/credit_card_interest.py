#All 3 problem sets for week 2.
# Working out compound interest, and repayments for min, and fixed payment options of increasing sophistication.
'''
Problem set 1
For each month:

Compute the monthly payment, based on the previous month’s balance.

Update the outstanding balance by removing the payment, then charging interest on the result.

Output the month, the minimum monthly payment and the remaining balance.

Keep track of the total amount of paid over all the past months so far.

Print out the result statement with the total amount paid and the remaining balance.

balance, annualInterestRate, monthlyPaymentRate

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''
balance = 484 #42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
def remainingBalance(balance, annualInterestRate, monthlyPaymentRate):
    """
    balance: int or float
    annualInterestRate: int or float
    monthlyPaymentRate: int or float
    returns: result; float of remaining balance if minimum monthly payment made for 12 months, rounded to 2 dec. places.
    """
    balanceLeft = balance
    monthlyInterestRate = annualInterestRate/12.0
    for month in range(12):
        monthlyPayment = balanceLeft * monthlyPaymentRate
        balanceLeft -= monthlyPayment
        balanceLeft += monthlyInterestRate * balanceLeft
    print("Remaining balance:", round(balanceLeft, 2))

remainingBalance(balance, annualInterestRate, monthlyPaymentRate)

'''
Problem set 2
Program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. fixed monthly payment is a single number which does not change each month, but instead is a constant amount that will be paid each month.

balance, annualInterestRate

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''
# balance = 3329
# annualInterestRate = 0.2
def lowestPayment(balance, annualInterestRate):
    """
    balance: int or float
    annualInterestRate: int or float
    returns: None. Prints result; float of lowest fixed payment to clear full balance in 12 months, rounded to 2 dec. places.
    """
    monthlyInterestRate = annualInterestRate/12.0
    monthlyPayment = 0
    balanceLeft = balance
    while balanceLeft > 0:
        balanceLeft = balance
        monthlyPayment += 10
        for month in range(12):
            balanceLeft -= monthlyPayment
            balanceLeft += monthlyInterestRate * balanceLeft
    print("Lowest Payment", round(monthlyPayment, 2))

lowestPayment(balance, annualInterestRate)

'''
Problem set 
ABSOLUTE VALUES and EPSILON CHECKS!!!!!!!!!!!!!
Program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. fixed monthly payment is a single number which does not change each month, but instead is a constant amount that will be paid each month.

balance, annualInterestRate

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''
#balance = 320000 # 29157.09
balance = 999999 # 90325.03
#annualInterestRate = 0.2
annualInterestRate = 0.18
def lowestPayment(balance, annualInterestRate):
    """
    balance: int or float
    annualInterestRate: int or float
    returns: None. Prints result; float of lowest fixed payment to clear full balance in 12 months to the cent, rounded to 2 dec. places.
    """
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyPaymentLowerBound = balance / 12
    monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
    epsilon = 0.01
    monthlyPayment = (monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2
    balanceLeft = balance
    while abs(balanceLeft) > epsilon:
        for month in range(12):
            balanceLeft -= monthlyPayment
            balanceLeft += monthlyInterestRate * balanceLeft
        if abs(balanceLeft) <= epsilon:
            break
        elif balanceLeft > 0:
            monthlyPaymentLowerBound = monthlyPayment
        else:
            monthlyPaymentUpperBound = monthlyPayment
        monthlyPayment = (monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2
        balanceLeft = balance
    print("Lowest Payment", round(monthlyPayment, 2))

lowestPayment(balance, annualInterestRate)
