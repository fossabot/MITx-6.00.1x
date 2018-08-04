# Simple demonstration of how to calculate how your money is going to last and return it in weeks

cash = 1700
fooddly = 15  # Daily food cost assuming $5 per meal
foodwkly = fooddly * 7
bills = 50  # Assumed weekly


def allowance(cash):
    weeks = 0
    weeklycost = foodwkly + bills
    while cash > weeklycost:
        cash -= weeklycost
        weeks += 1
    return weeks


print(allowance(cash))
