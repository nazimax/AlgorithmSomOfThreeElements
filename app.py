import math


def drawEtage(etage, T):
    begin = 2 ** etage - 1
    end = 2 * begin
    i = begin
    line=""
    height =int(math.floor(math.log(len(T), 2)))

    while i <= end:
        line =str(line) + str(T[i]) + " \t\t"
        i = i + 1

    print (height-etage)*"\t",line+"\n"


def drawTree(T):
    i = 0
    nbrEtage =math.floor(math.log(len(T),2))

    while i <= nbrEtage:
        drawEtage(i, T)
        i=i+1


# TODO finish heapsort
def left(i):
    if i == 0:
        return 0
    else:
        return 2 * i


def right(i):
    if i == 0:
        return 0
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
    temp = max(T) + 10
    T.insert(0, temp)
    i = (len(T) / 2)
    while i >= 0:
        heap(T, i)
        i = i - 1
    T.remove(temp)
    return T


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
        temp = list(T)
        temp.remove(T[k])

        i, j = sumTwoElements(temp, diff)
        if i != j:
            if (i >= k):
                i = i + 1
            if (j >= k):
                j = j + 1
            return k, i, j
        else:
            k = k + 1

    return -1, -1, -1


a = [20, 18, 17, 15, 12, 8, 4, 1]
b = [1, 2, 3, 4, 5,6,7]

drawTree(b)

# print sumOfThreeElements(a, 25)

# finished



#
# tocompile = "javac Main.java"
# run = "java Main"
#
#
# os.system(tocompile)
# os.system(run)
