# change coins using greedy

# A is denomination, T amount money
def change_coins(A, T):
    n = len(A)
    A.sort()
    print('list coins = ' + str(A))
    S = []  # solution: S[i] number of coins A[i]
    for i in range(0, len(A)):
        i = 0
        S.append(i)
    i = 0
    while (i <= n and T > 0):
        S[i] = T / A[i]
        T -= S[i] * A[i]
        i += 1

    if (T > 0):  # case for no solution
        return -1
    else:
        return S

def create_random_list_coins (n):  # n = size list coins
    for i in range(0, n):
        i = i + 1

    return 0

# hand create input list and amount money
A = [10, 2, 3, 4, 5, 6]
print("input list coin = " + str(A))
T = 50
print("T amount money = " + str(T))
print("solution: " + str(change_coins(A, T)))

# auto create input list and amount money
