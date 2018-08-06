import itertools

stuff = '123'
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        print(subset)


userboard = 'abcdefg'
wordstext = ['cab','deaf','johncena']
# Input is the word list, charset is userboard
def getPossibleWords(input,charSet):
    for word in input:
        wordsToPlay = []
        flag = 1
        if word not in charSet:
            flag = 0
        if flag==1:
            print(word)
            wordsToPlay.append(word)
    return wordsToPlay


print(getPossibleWords(wordstext,userboard))
