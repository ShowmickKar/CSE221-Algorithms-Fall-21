from file_io import read, write

"""
This code runs in O(n) in the best case
The reason being, during the first iteration of the outer loop, if the inner loop doesn't find two 
consecutive elements to swap, the outer loop breaks after the first pass
"""


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        check = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                check = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not check:
            break


a = read("task1-input1.txt")
bubble_sort(a)
write("task1-output1.txt", a)

b = read("task1-input2.txt")
bubble_sort(b)
write("task1-output2.txt", b)