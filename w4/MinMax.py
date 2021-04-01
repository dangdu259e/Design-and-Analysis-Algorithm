import numpy as np
import matplotlib.pyplot as plt
import time


def MinMax(a, L, R):
    if (R - L <= 1):
        return (min(a[L], a[R]), max(a[L], a[R]))
    else:
        (min1, max1) = MinMax(a, L, int((L + R) / 2))
        (min2, max2) = MinMax(a, int((L + R) / 2 + 1), R)
        return (min(min1, min2), max(max1, max2))


def createInputData(n):
    inputData = np.random.randint(-n, n, size=(n), dtype=int)
    return list(inputData)


def runTime(input):
    start = time.time()
    MinMax(input, 0, len(input) - 1)
    end = time.time()
    a_runtime = end - start
    return a_runtime


# dl
dl1 = createInputData(10)
dl2 = createInputData(10000)
dl3 = createInputData(1000000)

dl1_runtime = runTime(dl1)
dl2_runtime = runTime(dl2)
dl3_runtime = runTime(dl3)

#
# Data for plotting
input_size = (10, 100, 1000)
run_time = (dl1_runtime, dl2_runtime, dl3_runtime)

fig, ax = plt.subplots()
print(fig)
ax.plot(input_size, run_time)

ax.set(xlabel='input size', ylabel='run time (s)',
       title='Runtime MinMax Array')
ax.grid()

fig.savefig("MinMax.png")
plt.show()
