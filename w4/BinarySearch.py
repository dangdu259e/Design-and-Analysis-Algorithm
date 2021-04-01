import time
import matplotlib.pyplot as plt
import numpy as np


def binarySearch(inputData, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if inputData[mid] == x:
            return mid
        elif inputData[mid] > x:
            return binarySearch(inputData, l, mid - 1, x)
        else:
            return binarySearch(inputData, mid + 1, r, x)
    else:
        return -1

def createInputData(n):
    inputData = np.random.randint(-n, n, size=(n), dtype=int)
    return sorted(inputData)


def randomNumber(n):
    number = np.random.randint(-n, n, size=1)
    return int(number)


def runTime(input, random):
    start = time.time()
    binarySearch(input, 0, len(input) - 1, random)
    end = time.time()
    a_runtime = end - start
    return a_runtime


dl1 = createInputData(10)
random1 = randomNumber(10)

dl2 = createInputData(10000)
random2 = randomNumber(10000)

dl3 = createInputData(1000000)
random3 = randomNumber(1000000)

dl1_runtime = runTime(dl1, random1)
print(dl1_runtime)
dl2_runtime = runTime(dl2, random2)
print(dl2_runtime)

dl3_runtime = runTime(dl3, random3)
print(dl3_runtime)

#
# Data for plotting
input_size = (10, 100, 1000)
run_time = (dl1_runtime, dl2_runtime, dl3_runtime)

fig, ax = plt.subplots()
print(fig)
ax.plot(input_size, run_time)

ax.set(xlabel='input size', ylabel='run time (s)',
       title='Runtime find number by BinarySearch')
ax.grid()

fig.savefig("BinarySearch.png")
plt.show()
