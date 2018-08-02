import random

WORDLIST_FILENAME = "words.txt"
inFile = open(WORDLIST_FILENAME, 'r')
line = inFile.readline()
wordlist = line.split()

scrabbleLetterValue = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1, 'D': 2, 'G': 2,
                       'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}
playerHand = ''
playerPiecesCount = 10
usedLetters = ''


def wordScore(word):  # Gets the value of an input word
    points = 0
    global usedLetters
    for i in word:
        points += scrabbleLetterValue[i]
    if len(usedLetters) == playerPiecesCount:
        points *= len(word)  # Only do this if == player pieces count
    return points


def isValidWord(word):
    if word in wordlist:
        return True
    else:
        return False


def updateHand(word):
    global playerPiecesCount
    playerPiecesCount -= len(word)
    return playerPiecesCount


def randomLetter():
    return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


totalPoints = 0
# PLAY GAME
userChoice = ''
userBoard = ''
acceptableChoices = ['nre']
def playGame():
    global playerPiecesCount
    global totalPoints
    global userBoard
    global usedLetters
    while playerPiecesCount > 0:
        print('')
        playerHand = input(
            "Enter a word, or a '.' to indicate that you are finished: ").lower()        # while isValidWord(playerHand) == False:
        if playerHand == ".":
            print('')
            print("Ending game. You scored a total of " +
                str(totalPoints) + " total points.")
            print('')
            break
        elif isValidWord(playerHand):
            print("")
            x = 0  # wrong letter counter
            for i in playerHand.upper():
                if i not in userBoard:
                    x += 1
            if x == 0:
                totalPoints += wordScore(playerHand.upper())
                print('')
                print("You placed down the word " + "'" + playerHand.upper() + "'" +
                    " and you scored " + str(wordScore(playerHand.upper())) + " points.")
                print("You have " + str(totalPoints) + " total points.")
                print("")
                print("You have used the letters ")
                print("")
                playerHandAdd2Used = playerHand[:]
                usedLetters += playerHandAdd2Used
                for i in usedLetters:  # FIX USED LETTERS TODO
                    # prints words that we have used
                    print(i.upper(), ' ', end=' ', flush=True)
                for i in playerHand.upper():
                    if i in userBoard:   # Removes letters if played
                        userBoard = userBoard.replace(i, '', 1)
                    playerPiecesCount -= len(playerHand)
                print("")
                print("")
                print("Your hand is: ")
                print("")
                for i in userBoard:  # Prints user hand after incorrect entry
                    print(i, ' ', end='')
            else:
                print(
                    "Your word was in the dictionary but you don't have sufficient letters so it does not count.")
            print("")
            print("Your hand is: ")
            print("")
            for i in userBoard:  # Prints user hand after incorrect entry
                print(i, ' ', end='')

        else:
            print("I am sorry, that is not a valid entry. Please try again.")
            print("")
            print("Your hand is: ")
            print("")
            for i in userBoard:  # Prints user hand after incorrect entry
                print(i, ' ', end='')

def dealNewHand():
    while True:
        userChoice = input(
"Enter n to deal a new hand, r to replay the last hand, or e to end the game: ").lower()
        if userChoice == 'n':
            print("Deal a new hand")
            print('')
            print("New hand, coming right up!")
            print('')
            global userBoard
            userBoard = ''
            print("Your new hand is: ")
            print('')
            for i in range(0, (playerPiecesCount)):  # gets random letter
                userBoard = userBoard + randomLetter()
            for i in range(0, len(userBoard)):  # prints userboard
                print(userBoard[i], ' ', end='')
            playGame()
            break
        elif userChoice == 'r':
            print("Redoo the last hand")
        elif userChoice == 'e':
            print('')
            print('')
            print("Game Over")
            print('')
            print('')
            print("Thanks for playing!")
            break

dealNewHand()
