scores = [100, 97, 45, 90, 90, 76, 67, 28, 398, 97,
          45, 90, 100, 67, 80, 84, 85, 86, 87, 90, 90, 100]


def frequencyFinder(list):
    freq = {}
    for i in list:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq


print(frequencyFinder(scores))
