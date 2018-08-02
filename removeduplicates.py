L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 3, 4, 9]


def remove_dups(L1, L2):
    L1_Copy = L1[:]
    for i in L1_Copy:
        if i in L2:
            L1.remove(i)


remove_dups(L1, L2)

print(L1)
print(L2)
