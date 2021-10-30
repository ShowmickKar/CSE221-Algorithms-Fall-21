import time
import math
import matplotlib.pyplot as plt
import numpy as np


def fibonacci_1(n):
    if n <= 0:
        print("Invalid input!")
        return
    if n <= 2:
        return n - 1
    return fibonacci_1(n - 1) + fibonacci_1(n - 2)


def fibonacci_2(n):
    fibonacci_array = [0, 1]
    if n < 0:
        print("Invalid input!")
        return
    if n <= 2:
        return fibonacci_array[n - 1]
    for i in range(2, n):
        fibonacci_array.append(fibonacci_array[i - 1] + fibonacci_array[i - 2])
    return fibonacci_array[-1]


n = 40
x = [i for i in range(n)]
y = [0 for i in range(n)]
z = [0 for i in range(n)]

for i in range(n - 1):
    start = time.time()
    fibonacci_1(x[i + 1])
    y[i + 1] = time.time() - start
    start = time.time()
    fibonacci_2(x[i + 1])
    z[i + 1] = time.time() - start

x_interval = math.ceil(n / 10)
plt.plot(x, y, "r")
plt.plot(x, z, "b")
plt.xticks(np.arange(min(x), max(x) + 1, x_interval))
plt.xlabel("n-th position")
plt.ylabel("time")
plt.title("Comparing Time Complexity!")
plt.show()