from file_io import read, write


def selection_sort(a):
    for i in range(len(a) - 1):
        m = a[i]
        index = i
        for j in range(i + 1, len(a)):
            if a[j] < m:
                m = a[j]
                index = j
        if m < a[i]:
            a[i], a[index] = a[index], a[i]


a = read("task2-input1.txt")
selection_sort(a)
write("task2-output1.txt", a)

b = read("task2-input2.txt")
selection_sort(b)
write("task2-output2.txt", b)