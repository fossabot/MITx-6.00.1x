# Moves some things around, idk

def printMove(fr, to):
    print("Move from ", str(fr), " to ", str(to))


def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)


print(Towers(6, "P1", "P2", "P3"))
