def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def heap(T, i):
    lef = left(i)
    righ = right(i)
    if lef < len(T) and T[lef] > T[i]:
        max = lef
    else:
        max = i
    if righ < len(T) and T[righ] > T[i]:
        max = righ
    if max != i:
        T[max], T[i] = T[i], T[max]
        heap(T, max)


def buildHeap(T):
    i=len(T)/2
    return 0
