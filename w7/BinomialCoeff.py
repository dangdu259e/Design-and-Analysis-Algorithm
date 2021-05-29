# Binomial Coef with recursion
def binomialCoeff(n, k):
    if (k == 0 or k == n):
        return 1
    elif (k > n):
        return 0
    else:
        return binomialCoeff(n - 1, k - 1) + binomialCoeff(n - 1, k)

print(binomialCoeff(5, 2))
