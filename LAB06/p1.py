"""
Task 01
"""


def helper(s1, s2, i, j, dp):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        if dp[i][j] < 0:
            dp[i][j] = 1 + helper(s1, s2, i + 1, j + 1, dp)
        return dp[i][j]
    else:
        if dp[i][j] < 0:
            res1 = helper(s1, s2, i + 1, j, dp)
            res2 = helper(s1, s2, i, j + 1, dp)
            dp[i][j] = max(res1, res2)
        return dp[i][j]


def longest_common_subsequence(s1, s2):
    s1 += "0"
    s2 += "0"
    dp = [[-1 for j in range(len(s2))] for i in range(len(s1))]
    helper(s1, s2, 0, 0, dp)
    ans = ""
    i = 0
    j = 0
    while i < len(s1) - 1 and j < len(s2) - 1:
        if s1[i] == s2[j]:
            ans += s1[i]
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1

    return ans


def read():
    prediction = {}
    actual = {}
    file = open("input1.txt", "r")
    for line in file:
        zone = line.split(" ")
        if len(zone) < 3:
            break
        if zone[2][-1] == "\n":
            zone[2] = zone[2][:-1]
        # print(zone)
        prediction[zone[1]] = zone[2]

    for line in file:
        zone = line.split(" ")
        if zone[2][-1] == "\n":
            zone[2] = zone[2][:-1]
        actual[zone[1]] = zone[2]
    file.close()
    return prediction, actual


def write(lcs, actual, string1):
    file = open("output1.txt", "w")
    for letter in lcs:
        file.write(f"{actual[letter]} ")
    file.write(f"\nCorrectness of prediction: {(len(lcs * 100)/len(string1))}%")
    file.close()


prediction, actual = read()
# print(f"Prediction: {prediction} Actual: {actual}")
string1 = ""
string2 = ""
for c in prediction:
    string1 += c
for c in actual:
    string2 += c

lcs = longest_common_subsequence(string1, string2)
write(lcs, actual, string1)