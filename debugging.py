# def integerDivision(x, a):
#     """
#     x: a non-negative integer argument
#     a: a positive integer argument

#     returns: integer, the integer division of x divided by a.
#     """
#     while x >= a:
#         count += 1
#         x = x - a
#     return count
# OLD

# NEW
def integerDivisionNew(x, a):
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

print(integerDivisionNew(10,5))