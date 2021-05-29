def binomialCoefDP(n, k):
    # create result table
    C = []
    for i in range(0, n + 1):
        C.append([])
        for j in range(0, k + 1):
            C[i].append(0)
    # create result table
    # C = [[0 for x in range(k + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k], C
number, C = binomialCoefDP(5, 3)
print(C)
print(number)
