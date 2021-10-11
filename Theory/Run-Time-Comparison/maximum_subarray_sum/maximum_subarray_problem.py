import math
import time
import random
from datetime import datetime
from matplotlib import pyplot as plt


def max_crossing_sum(a, l, h, m):
    left_sum = 0
    right_sum = 0
    sum = 0
    i = m
    while i >= l:
        sum += a[i]
        left_sum = max(sum, left_sum)
        i -= 1
    sum = 0
    i = m + 1
    while i < h:
        sum += a[i]
        right_sum = max(sum, right_sum)
        i += 1
    return left_sum + right_sum


def maximum_subarray(a, l, h):
    if l + 1 == h:
        return a[l]
    m = (l + h) // 2
    return max(
        maximum_subarray(a, l, m),
        maximum_subarray(a, m, h),
        max_crossing_sum(a, l, h, m),
    )


def maximum_subarray_bruteforce(a):
    n = len(a)
    result = -math.inf
    for i in range(0, n):
        sum = 0
        for j in range(i, n):
            sum += a[j]
            result = max(sum, a[j], result)
    return result


def kadens_algorithm(a):
    n = len(a)
    best = -math.inf
    best_here = 0
    for i in range(n):
        best_here = best_here + a[i]
        if best < best_here:
            best = best_here
        if best_here < 0:
            best_here = 0
    return best


array_container = [
    [random.randint(-5000, 5000) for j in range(1, i * 100)] for i in range(100)
]


time_brute_force = []
time_kadens_algorithm = []