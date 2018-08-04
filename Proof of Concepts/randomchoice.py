import random

def randomLetter():  # Gets a random letter
    r = random.randint(1,10)
    letter = ''
    if r <= 5:
        letter = random.choice('AEIOU')
    else:
        letter = random.choice('BCDFGHJKLMNPQRSTVWXYZ')
    print(r)
    return letter

print(randomLetter())
