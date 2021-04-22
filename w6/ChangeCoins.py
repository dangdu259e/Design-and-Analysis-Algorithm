# change coins using greedy
import random

import numpy as np


# A is denomination, T amount money
def change_coins(A, T):
    n = len(A)  # size of list denomination
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


def create_random_list_coins(n):  # n = size list coins
    A = list(range(1, n))
    random.shuffle(A)
    return A


# hand create input list and amount money
print("handle create input list and amount money")
A = [10, 2, 3, 4, 5, 6]
print("input list coin = " + str(A))
T = 50
print("T amount money = " + str(T))
print("solution: " + str(change_coins(A, T)))

print("-------------------------------")

# random input
print("random input")
a = create_random_list_coins(10)
print("input list coin = " + str(a))
t = np.random.randint(1, 100, dtype=int)  # create random amount money
print("T amount money = " + str(t))
print("solution: " + str(change_coins(a, t)))

# auto create input list and amount money
