def maxium_value_ls(a, n):
    result = [1] * n
    for i in range(0, n):
        for j in range(0, i):
            if (a[i] > a[j] and result[i] < result[j] + 1):
                result[i] += 1
    return max(result), result


def findSolution(max, result, a):
    position = 0
    solution = []
    for i in range(0, len(result)):
        if (result[i] == max):
            position = i
    for i in range(position, 0, -1):
        if (result[i] == (result[i - 1] + 1)):
            solution.append(i - 1)
    return solution


# input ls
a = [1, 2, 5, 4, 6, 3, 8, 9, 7]
max, result = maxium_value_ls(a, len(a))
print(max)
print(result)
print(findSolution(max, result, a))
