# TODO finish heapsort
def left(i):
    if i == 0:
        return 1
    else:
        return 2 * i


def right(i):
    if i == 0:
        return 2
    else:
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
    i = (len(T) / 2)
    while i >= 0:
        heap(T, i)
        i = i - 1
    return 0


# we suppose that heapsort is done now start the alorithm
# we test it with sorted array


# these two functions return the indexes of numbers

def sumTwoElements(T, toFind):
    fromRight = len(T) - 1
    fromLeft = 0
    i = 0
    som = T[fromLeft] + T[fromRight]
    while som != toFind and fromLeft < fromRight:
        if som > toFind:
            fromLeft = fromLeft + 1
            som = T[fromLeft] + T[fromRight]
        else:
            fromRight = fromRight - 1
            som = T[fromLeft] + T[fromRight]

    if fromLeft < fromRight:
        return fromLeft, fromRight
    else:
        return -1, -1


def sumOfThreeElements(T, toFind):
    k = 0
    i, j = -1, -1
    while k < len(T):
        diff = toFind - T[k]
        temp = T
        temp.remove(T[k])
        i, j = sumTwoElements(temp, diff)
        if i != j:
            return k, i, j
        else:
            k = k + 1

    return -1, -1, -1


a = [20, 18, 17, 15, 12, 8, 4, 1]

print sumOfThreeElements(a, 32)

# finished
