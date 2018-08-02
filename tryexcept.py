while True:
    try:
        n = input("Give me a number: ")
        n = int(n)
        break
    except ValueError:
        print("You didn't put an integer, try again!")
print("Nice number you picked boi")
