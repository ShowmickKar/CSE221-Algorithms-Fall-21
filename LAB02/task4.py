from file_io import read, write


def merge(a, p, q, r, b):
    left = p
    right = q + 1
    index = p
    while index <= r:
        try:
            if left <= q and (right > r or a[left] <= a[right]):
                b[index] = a[left]
                left += 1
            else:
                b[index] = a[right]
                right += 1
        except:
            print(left, right, index, len(a))
        index += 1
    for i in range(len(a)):
        a[i] = b[i]


def merge_sort(a, p, r, b=[]):
    if p >= r:
        return
    if not len(b):
        b = [a[i] for i in range(len(a))]
    q = (p + r) // 2
    merge_sort(a, p, q, b)
    merge_sort(a, q + 1, r, b)
    merge(a, p, q, r, b)
    return b


a = read("task4-input1.txt")
a = merge_sort(a, 0, len(a) - 1)
write("task4-output1.txt", a)

b = read("task4-input2.txt")
b = merge_sort(b, 0, len(b) - 1)
write("task4-output2.txt", b)