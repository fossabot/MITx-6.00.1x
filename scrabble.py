import random
# TODO add a computer player that gets the best word, name it as hint
# TODO add functionality to play last hand
WORDLIST_FILENAME = "words.txt"
inFile = open(WORDLIST_FILENAME, 'r')
line = inFile.readline()
wordlist = line.split()

scrabbleLetterValue = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3,
                       'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
playerHand = ''  # keeps track of hand that player played
playerPiecesCount = 1  # how many pieces to deal at the start of the game
usedLetters = ''  # keeps track of letters used

# Gets the value of a word


def wordScore(word):
    points = 0
    global usedLetters
    for i in word:
        points += scrabbleLetterValue[i]
    if len(usedLetters) == playerPiecesCount:
        # Only do this if == player pieces count
        points *= len(word)
        # call a function here saying that you won, WINNING CONDITION
    return points

# Checks if the word you played was in the dictionary


def isValidWord(word):
    if word in wordlist:
        return True
    else:
        return False

# Reduces pieces by the length of the word that was played


def updateHand(word):
    global playerPiecesCount
    playerPiecesCount -= len(word)
    return playerPiecesCount


def randomLetter():  # Gets a random letter
    r = random.randint(1, 10)
    letter = ''
    if r <= 5:
        letter = random.choice('AEIOU')
    else:
        letter = random.choice('BCDFGHJKLMNPQRSTVWXYZ')
    return letter


totalPoints = 0

# The board that the user gets from randomLetter
userBoard = ''
# Initial user input to start the game
userChoice = ''
# Acceptable inputs for userChoice
acceptableChoices = ['nre']

# Prints user hand after incorrect entry


def showUserHand(userBoard):
    for i in userBoard:
        print(i, ' ', end='')

# Give user his words


def giveWords():
    global userBoard
    for i in range(0, (playerPiecesCount)):
        userBoard = userBoard + randomLetter()


def printUserWords():
    for i in range(0, len(userBoard)):
        print(userBoard[i], ' ', end='')


def invalidEntryPrompt():
    print("I am sorry, that is not a valid entry. Please try again.")
    print()
    print("Your hand is: ")
    print()



def playGame():
    global playerPiecesCount
    global totalPoints
    global userBoard
    global usedLetters

    while playerPiecesCount > 0:
        print()
        # Keep asking for input as long as its invalid
        playerHand = input(
            "Enter a word, or a '.' to indicate that you are finished: ").lower()
        if playerHand == ".":
            print()
            # Prints ending message in singular since the player only has 1 point
            if totalPoints == 1:
                print("Ending game. You only scored",
                      str(totalPoints), "point.")
                print()
            else:
                print("Ending game. You scored a total of ",
                      str(totalPoints), " total points.")
                print()
            break
        # Checks if the word you inputted is in dictionary
        elif isValidWord(playerHand):
            print()
            # Wrong letter counter
            x = 0
            for i in playerHand.upper():
                if i not in userBoard:
                    x += 1
            # If no words are wrong
            if x == 0:
                totalPoints += wordScore(playerHand.upper())
                print()
                print("You placed down the word '", playerHand.upper(
                ), "' and you scored ", str(wordScore(playerHand.upper())), " points.")
                # Decrements player pieces
                playerPiecesCount -= len(playerHand)
                # Winning condition
                if playerPiecesCount == 0:
                    print()
                    print("Congratulations! You've won the game. You scored a total of ",
                          totalPoints, "points. I hope you enjoyed playing!")
                    break
                else:
                    print("You have ", str(totalPoints), " total points.")
                    print()
                    print("You have used the letters ")
                    print()
                    # Add the letters that we used to usedLetters
                    playerHandAdd2Used = playerHand[:]
                    usedLetters += playerHandAdd2Used
                    for i in usedLetters:
                        # Prints words that we have used
                        print(i.upper(), ' ', end=' ', flush=True)
                    for i in playerHand.upper():
                        # Removes letters if played
                        if i in userBoard:
                            userBoard = userBoard.replace(i, '', 1)

            else:
                print(
                    "Your word was in the dictionary but you don't have sufficient letters so it does not count.")

            print()
            print("Your hand is: ")
            print()
            # Prints user hand after incorrect entry
            showUserHand(userBoard)

        else:
            invalidEntryPrompt()

            # Prints user hand after incorrect entry
            showUserHand(userBoard)


def gameOverPrompt():
    print()
    print()
    print("Game Over")
    print()
    print()
    print("Thanks for playing!")

# Deals new hand


def dealNewHand():
    print("Deal a new hand")
    print()
    print("New hand, coming right up!")
    print()
    global userBoard
    userBoard = ''
    print("Your new hand is: ")
    print()
    # Gives user his words
    giveWords()
    # Prints the letters that were given
    printUserWords()


def start():
    global playerPiecesCount
    # Checks if letters is a number
    while True:
        try:
            playerPiecesCount = abs(int(
                input("Please input how many letters you want dealt. ")))
            if playerPiecesCount > 1:
                print("You've selected to play with",
                      playerPiecesCount, "letters.")
                break
            else:
                print("You've selected to play with only",
                      playerPiecesCount, "letter. Oh boy. Here we go...")
                break
            break
        except ValueError:
            print("Please enter whole number.")
            continue
    while True:
        try:
            userChoice = str(input(
                "Enter n to deal a new hand, r to replay the last hand, or e to end the game: "))
            userChoice = userChoice.lower()
            if userChoice == 'n':
                dealNewHand()
                playGame()
            elif userChoice == 'r':
                print("Redoo the last hand")
                # Call function here
                break
            elif userChoice == 'e':
                gameOverPrompt()
                break
        except ValueError:
            print("Eother value eaERROR nd, or e to end the game: ")
            continue


start()

# getBestHand():
#     for