"""
Task 02
"""


def helper(s1, s2, s3, i, j, k, dp):
    if i == len(s1) or j == len(s2) or k == len(s3):
        return 0
    elif s1[i] == s2[j] and s2[j] == s3[k] and dp[i][j][k] < 0:
        dp[i][j][k] = 1 + helper(s1, s2, s3, i + 1, j + 1, k + 1, dp)
    elif dp[i][j][k] < 0:
        dp[i][j][k] = max(
            helper(s1, s2, s3, i + 1, j, k, dp),
            max(
                helper(s1, s2, s3, i, j + 1, k, dp), helper(s1, s2, s3, i, j, k + 1, dp)
            ),
        )
    return dp[i][j][k]


def longest_common_subsequence(s1, s2, s3):
    dp = [
        [[-1 for k in range(len(s3))] for j in range(len(s2))] for i in range(len(s1))
    ]

    return helper(s1, s2, s3, 0, 0, 0, dp)


def read():
    file = open("input2.txt")
    strings = []
    for line in file:
        strings.append(line)
    return strings
    file.close()


def write(result):
    file = open("output2.txt", "w")
    file.write(str(result))
    file.close()


strings = read()

write(longest_common_subsequence(strings[0], strings[1], strings[2]))
