import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

for n in range(n+1):
    if n <= 1:
        dp[n] = n
    else:
        dp[n] = dp[n-1] + dp[n-2]

print(dp[n])