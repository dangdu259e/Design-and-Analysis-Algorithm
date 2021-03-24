import time
import matplotlib.pyplot as plt


def move1Disk(A, B):
    print("{} -> {} \n".format(A, B))


def moveTower(n, a, b, c):
    if (n == 1):
        move1Disk(a, b)
    else:
        moveTower(n - 1, a, c, b)
        move1Disk(a, b)
        moveTower(n - 1, c, b, a)


def timeRunning(n):
    start = time.time()
    moveTower(n, 'A', 'B', 'C')
    end = time.time()
    n_runtime = end - start
    return n_runtime


dl1 = 5
dl2 = 10
dl3 = 15

dl1_runtime = timeRunning(dl1)
dl2_runtime = timeRunning(dl2)
dl3_runtime = timeRunning(dl3)

# Data for plotting
input_size = (dl1, dl2, dl3)
run_time = (dl1_runtime, dl2_runtime, dl3_runtime)

fig, ax = plt.subplots()
print(fig)
ax.plot(input_size, run_time)

ax.set(xlabel='input size', ylabel='run time (s)',
       title='Runtime find MoveTower')
ax.grid()

fig.savefig("MoveTower.png")
plt.show()
