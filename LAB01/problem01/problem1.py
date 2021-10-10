"""
Problem 01: File I/O
"""

# Global variable
odd = 0
even = 0
no_parity = 0
palindrome = 0
non_palindrome = 0

# returns true if the input string in palindrome
def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def write_to_output(inputs):
    global odd, even, no_parity, palindrome, non_palindrome
    print("Writing to output.txt..")
    output_file = open("output.txt", "w")
    for input in inputs:
        output = " "
        num, s = input[0], input[1]
        output += f"{num} "
        if isinstance(num, int):
            if num % 2 == 0:
                even += 1
                output += "has even parity "
            else:
                odd += 1
                output += "has odd parity "
        else:
            no_parity += 1
            output += "cannot have parity "
        output += f"and {s} is "
        if is_palindrome(s):
            palindrome += 1
            output += "a palindrome\n"
        else:
            non_palindrome += 1
            output += "not a palindrome\n"
        output_file.writelines(output)
    output_file.close()


def write_to_record():
    print("Writing to record.txt..")
    record_file = open("record.txt", "w")
    record_file.writelines(
        f"Percentage of odd parity: {((odd/(odd + even + no_parity)) * 100)}%\n"
    )
    record_file.writelines(
        f"Percentage of even parity: {((even/(odd + even + no_parity)) * 100)}%\n"
    )
    record_file.writelines(
        f"Percentage of no parity: {((no_parity/(odd + even + no_parity)) * 100)}%\n"
    )
    record_file.writelines(
        f"Percentage of palindrome: {(palindrome/(palindrome + non_palindrome)) * 100}%\n"
    )
    record_file.writelines(
        f"Percentage of palindrome: {(non_palindrome/(palindrome + non_palindrome)) * 100}%\n"
    )
    record_file.close()
    print("...done")


def read_from_file():
    print("Reading input from input.txt...")
    input_file = open("input.txt", "r")
    inputs = []
    for line in input_file:
        inputs.append(line.split())
        try:
            inputs[-1][0] = int(inputs[-1][0])
        except:
            inputs[-1][0] = float(inputs[-1][0])
    input_file.close()
    return inputs


inputs = read_from_file()
write_to_output(inputs)
write_to_record()