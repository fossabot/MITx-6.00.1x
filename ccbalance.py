bal = input("What is your credit card balance?")
while bal!= int or bal != float:
    print("That is not a valid entry.")
    if:
        bal == 

try:
    rate = float((input("What is your credit card interest rate?")))
except ValueError:
    print("That is not a valid entry.")

try:
    mPay = float((input("What is your average monthly payment?")))
except ValueError:
    print("That is not a valid entry.")


# Checks how long it will take to pay off a CC
def calcPayment(balance, rate, mPay):
    months = 0
    while balance > 0:
        balance = (balance-mPay) * (1+((rate/100)/12))
        months += 1
    print("It would take you ", str(months), " months to pay off a balance of $", str(
        bal), " while making monthly payments of $", str(mPay), " at an interest rate of ", str(rate), "%.", sep='')


calcPayment(bal, rate, mPay)
