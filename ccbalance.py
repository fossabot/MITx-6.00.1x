bal = float((input("What is your credit card balance?")))
rate = float((input("What is your credit card interest rate?")))
mPay = float((input("What is your average monthly payment?")))

def calcPayment(balance,rate,mPay):
    months = 0
    while balance > 0:
        balance = (balance-mPay) * (1+((rate/100)/12))
        months += 1
    print("It would take you " + str(months) + " months to pay off a balance of " + "$" + str(bal) + " while making monthly payments of " + "$" + str(mPay) + " at an interest rate of " + str(rate) + "%.")

calcPayment(bal,rate,mPay)
