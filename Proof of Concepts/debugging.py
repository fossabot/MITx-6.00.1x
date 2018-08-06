def integerDivisionNew(x, a):
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count


print(integerDivisionNew(10, 5))
