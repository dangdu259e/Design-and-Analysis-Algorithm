def BruteForceStringMatching(text, pattern):
    # String matching problem
    # Brute Force algorithm
    n = len(text)
    m = len(pattern)

    for i in range(0, n - m + 1):
        j = 0
        while ((j < m) and (pattern[j] == text[i + j])):
            j = j + 1
        if (j == m):
            return i
    return -1

text = "adbcbdc"
pattern = "dc"
print(BruteForceStringMatching(text, pattern))
