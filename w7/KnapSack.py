# input
W = [12, 2, 1, 1, 4]  # Weight
V = [4, 2, 1, 2, 10]  # Value
M = 15  # Max Weight
n = len(W) - 1  # length of items


# method
def KnapSack(W, V, M, n):
    # create Result table v1
    C = []
    maxium = 0  # max value
    position = (0, 0)  # position max value
    for i in range(0, n + 1):
        C.append([])
        for j in range(0, M + 1):
            C[i].append(0)

    # create Result table v2
    # C = [[0 for i in range (0, M+1)] for i in range(0, n+1)]

    # insert value to result table
    for i in range(n + 1):
        for j in range(M + 1):

            # row 0 or column 0 ==> value in result table = 0
            if (i == 0 or j == 0):
                C[i][j] = 0

            # another value using Recurrence relation formular
            elif (W[i] <= j):
                C[i][j] = max(C[i - 1][j], C[i - 1][j - W[i]] + V[i])
                if (C[i][j] > maxium):
                    maxium = C[i][j]
    return C, maxium


# Back-trace to indicate the solution
def findSolution(W, C):
    listiteams = []
    i = len(C) - 1
    j = len(C[0]) - 1
    for x in range(i, 0, -1):
        if (C[x][j] != C[x - 1][j]):
            listiteams.append(x)
            j = j - W[i]

    return listiteams


def printResultTable(C):
    for i in range(len(C)):
        for j in C[i]:
            print(C[i][j], end='\t')
        print(" ")


C, maxium = KnapSack(W, V, M, n)
print("result table: ")
printResultTable(C)
print('--------------')
print("MaxValue: " + str(maxium))
print("solution: ", findSolution(W, C))
