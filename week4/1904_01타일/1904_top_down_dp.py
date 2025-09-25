import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
dp = [-1] * (n+1)
def recur(length):

    if length > n:
        return 0

    if length == n:
        return 1

    if dp[length] != -1:
        return dp[length]

    dp[length] = (recur(length + 2) + recur(length + 1)) % 15746

    return dp[length]

print(recur(0))

