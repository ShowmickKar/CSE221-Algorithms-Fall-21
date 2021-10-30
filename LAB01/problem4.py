"""
Problem 04: Matrix Multiplication
"""


def multiply_matrix(a, b):
    n = len(a)
    c = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

def read_input():
    print("Reading Matrix A from input file...")
    file_a = open("input_A.txt", "r")
    
    print("Reading Matrix B from input file...")
    file_b = open("input_B.txt", "r")
    
    a = []
    b = []
    for row in file_a:
        cur_row = row.split(' ')
        for i in range(len(cur_row)):
            cur_row[i] = int(cur_row[i])
        a.append(cur_row)
    
    for row in file_b:
        cur_row = row.split(' ')
        for i in range(len(cur_row)):
            cur_row[i] = int(cur_row[i])
        b.append(cur_row)
    file_a.close()
    file_b.close()
    return a, b

def write_to_output(c):
    print("Writing result to output file...")
    output_file = open("output_product.txt", "w")    
    for row in c:
        row_str = ""
        for element in row:
            row_str += str(element) + " "
        row_str += "\n"
        output_file.write(row_str)
            
    output_file.close()
    
    
if __name__ == "__main__":
    a, b = read_input()
    print("Calculating the product....")
    c = multiply_matrix(a, b)
    write_to_output(c)
    print("...done")