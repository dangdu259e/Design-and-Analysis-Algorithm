def LongestIncreasingSubsequence(a):
    LIS = 1
    for i in range(0, len(a)):
        LIS = max(LIS, LIS_ending_number(a, i))
    return LIS


def LIS_ending_number(a, current):
    if (a == 0):
        return 1
    ans = 1
    for i in range(current - 1, -1, -1):
        if (a[i] < a[current]):
            ans = max(ans, 1 + LIS_ending_number(a, i))
    return ans


# test case
a = [1, 2, 5, 4, 6, 3, 8, 9, 7]
print("input: ", a)
print("Longest Increasing Subsequence is ", LongestIncreasingSubsequence(a))
