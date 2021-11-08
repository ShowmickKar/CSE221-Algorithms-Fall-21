"""
All the tasks in this lab invokes the read function and read input from file
and invoke the write function to write output to designated file
"""


def read(filename):
    file = open("tests/" + filename, "r")
    n = file.readline()
    a = file.readline().split(" ")
    for i in range(len(a)):
        a[i] = int(a[i])
    b = file.readline().split()
    file.close()
    if len(b):
        for i in range(len(b)):
            b[i] = int(b[i])
        return a, b
    return a


def write(filename, content):
    file = open("tests/" + filename, "w")
    for e in content:
        file.write(f"{e} ")
    file.close()
