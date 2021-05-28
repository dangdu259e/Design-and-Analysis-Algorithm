# find Longest Increasing Subsequence
def maxium_value_ls(a, n):
    # create result table
    result = [1] * n
    for i in range(0, n):
        for j in range(0, i):
            # update result table
            if (a[i] > a[j] and result[i] < result[j] + 1):
                result[i] += 1
    return max(result), result


# solution of LIS
def findSolution(max, result, a):
    position = 0
    pos_solution = []
    solution = []
    for i in range(0, len(result)):
        if (result[i] == max):
            position = i
    pos_solution.append(position)
    solution.append(a[position])
    for i in range(position, 0, -1):
        if (result[position] == (result[i - 1] + 1)):
            position = i - 1
            pos_solution.append(i - 1)
            solution.append(a[position])

    return solution


def formatSolution(solution):
    result = []
    for i in range(0, len(solution)):
        result.append(solution.pop())
    return result


# input
a = [1, 2, 5, 4, 6, 3, 8, 9, 7]
print("input: ", a)
max, result = maxium_value_ls(a, len(a))
print("Longest Increasing Subsequence: ", max)
solution = findSolution(max, result, a)
solution_format = formatSolution(solution)
print("Solution: ", solution_format)
