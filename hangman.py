# Gets a random word from a list
import random
WORDLIST_FILENAME = "words.txt"
inFile = open(WORDLIST_FILENAME, 'r')
line = inFile.readline()
wordlist = line.split()


# Prints intro greeting
def hangman(word):
    turns = 10
    userName = input(
        "Hello and welcome to Joswayski's Hangman. What is your name? ")
    print('')
    print("Hi " + userName + "! I hope you enjoy playing. Your first word has " + str(len(word)) +
                     " letters.\n \nIt's time to start. If you input more than one letter, I will automaitcally grab the first one. Good luck!")

    print('')
# Prints how many turns we have left
    guesses = ''
    for i in word:
        print(" _ ")
    print('')
    if turns == 1:
        print("You have " + str(turns) + " guess left.")
    elif turns >= 2:
        print("You have " + str(turns) + " guesses left.")

# blank
    print('')

    while turns > 0:
        failed = 0
        # defines acceptable imputs
        acceptableInputs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        userGuess = input("Guess a letter: ")
        # checks if user imputted anything at all
        while userGuess == '':
            userGuess = input("You must type a letter: ")
            # if user imputs more than one thing, get the first index
        userGuess = userGuess[0].lower()
        while userGuess[0].lower() not in acceptableInputs:
            print("Only letters A - Z are allowed. Try again.")
            userGuess = input("Guess a letter: ")
            # checks if user imputted that same thing already
        if userGuess in guesses:
            print("You said '" + userGuess + "' already. Try again.")
            # if user is correct
        elif userGuess in word:
            print("Correct!")
            # if user is wrong
        elif userGuess not in word:
            print("Wrong!")
            turns -= 1
            if turns == 1:
                print("Sorry, your guess is not in this word. Try again. You have " +
                      str(turns) + " guess left.")
            elif turns >= 2:
                print("Sorry, your guess is not in this word. Try again. You have " +
                      str(turns) + " guesses left.")
                # if user is out of turns, end the game
            else:
                print("GAME OVER")
                print("Your word was: " + word)
                break
            # adds userguess to guesses list
        for char in word:
            guesses += userGuess
            if char in guesses:
                print(char)
                # prints a blank space if letter hasnt been guessed
            else:
                print(" _ ")
                failed += 1
                # if you win the game
        if failed == 0:
            print("CONGRATULATIONS! YOU DID IT!")
            break

# calls hangman with an imput using a random word from our words.txt
hangman(random.choice(wordlist))
