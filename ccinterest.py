while True:
    try:
        bal = float(input("What is your credit card balance?"))
    except ValueError:
        print("I'm sorry, I dont understand.")
        continue
    else:
        break

while True:
    try:
        rate = float(input("What is your credit card interest rate?"))
    except ValueError:
        print("I'm sorry, I dont understand.")
        continue
    else:
        break

while True:
    try:
        mPay = float(input("What is your average monthly payment?"))
    except ValueError:
        print("I'm sorry, I dont understand.")
        continue
    else:
        break


# Checks how long it will take to pay off a CC
def calcPayment(balance, rate, mPay):
    months = 0
    while balance > 0:
        balance = (balance-mPay) * (1+((rate/100)/12))
        months += 1
    print("It would take you ", str(months), " months to pay off a balance of $", str(
        bal), " while making monthly payments of $", str(mPay), " at an interest rate of ", str(rate), "%.", sep='')


calcPayment(bal, rate, mPay)
