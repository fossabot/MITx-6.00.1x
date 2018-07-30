import random

WORDLIST_FILENAME = "words.txt"

inFile = open(WORDLIST_FILENAME, 'r')

line = inFile.readline()

wordlist = line.split()

def hangman(word):
    turns = 10
    userName = input("Hello and welcome to Joswayski's Hangman. What is your name? ")
    print('')
    greeting = print("Hi " + userName + "! I hope you enjoy playing. Your first word has " + str(len(word)) +
                     " letters.\n \nIt's time to start. If you input more than one letter, I will automaitcally grab the first one. Good luck!")

    print('')

    guesses = ''
    for letters in word:
        print(" _ ")
    print('')
    if turns == 1:
        print("You have " + str(turns) + " guess left.")
    elif turns >= 2:
        print("You have " + str(turns) + " guesses left.")

    print('')

    while turns > 0:
        failed = 0
        acceptableInputs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        userGuess = input("Guess a letter: ")
        while userGuess == '':
            userGuess = input("You must type a letter: ")
        userGuess = userGuess[0].lower()
        while userGuess[0].lower() not in acceptableInputs:
            print("Only letters A - Z are allowed. Try again.")
            userGuess = input("Guess a letter: ")
        if userGuess in guesses:
            print("You said '" + userGuess + "' already. Try again.")
        elif userGuess in word:
            print("Correct!")
        elif userGuess not in word:
            print("Wrong!")
            turns -= 1
            if turns == 1:
                print("Sorry, your guess is not in this word. Try again. You have " + str(turns) + " guess left.")
            elif turns >= 2:
                print("Sorry, your guess is not in this word. Try again. You have " + str(turns) + " guesses left.")
            else:
                print("GAME OVER")
                print("Your word was: " + word)
                break
        for char in word:
            guesses += userGuess  # adds userguess to guesses list
            if char in guesses:
                print(char)
            else:
                print(" _ ")
                failed += 1
        if failed == 0:
            print("CONGRATULATIONS! YOU DID IT!")
            break
        
hangman(random.choice(wordlist))
