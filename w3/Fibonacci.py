import time

import matplotlib.pyplot as plt

def fibonacci(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def runTime(a):
    start = time.time()
    fibonacci(a)
    end = time.time()
    a_runtime = end - start
    return a_runtime


dl1 = 5
dl2 = 20
dl3 = 35

dl1_runtime = runTime(dl1)
dl2_runtime = runTime(dl2)
dl3_runtime = runTime(dl3)

# Data for plotting
input_size = (dl1, dl2, dl3)
run_time = (dl1_runtime, dl2_runtime, dl3_runtime)

fig, ax = plt.subplots()
print(fig)
ax.plot(input_size, run_time)

ax.set(xlabel='input size', ylabel='run time (s)',
       title='Runtime find Fibonacci')
ax.grid()

fig.savefig("Fibonacci.png")
plt.show()
