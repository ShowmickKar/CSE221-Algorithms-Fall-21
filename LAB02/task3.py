from file_io import read, write


def insertion_sort(a, b):
    for i in range(1, len(b)):
        j = i - 1
        cur_a = a[i]
        cur_b = b[i]
        while j >= 0 and cur_b > b[j]:
            a[j + 1] = a[j]
            a[j] = cur_a
            b[j + 1] = b[j]
            b[j] = cur_b
            j -= 1


a, b = read("task3-input1.txt")
insertion_sort(a, b)
write("task3-output1.txt", a)

c, d = read("task3-input2.txt")
insertion_sort(c, d)
write("task3-output2.txt", c)