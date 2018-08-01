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


def wordScore(word): ## Gets the value of an input word
    points = 0
    global usedLetters
    for i in word:
            points += scrabbleLetterValue[i]
            usedLetters = usedLetters + i
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

# PLAY GAME
while playerPiecesCount > 0:
    playerHand = input("Put down a word: ").lower()
    if isValidWord(playerHand) == True:
        print("You placed down the word " + playerHand + " and you scored " + str(wordScore(playerHand.upper())) + " points." )
        playerPiecesCount -= len(playerHand)
    else:
        playerHand = input("I am sorry. That word is not valid. Try again.").lower()




