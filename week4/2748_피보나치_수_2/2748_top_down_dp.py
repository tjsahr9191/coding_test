import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
dp = [-1] * (n + 1)
def fibo(n):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fibo(n-1) + fibo(n-2)

    return dp[n]

print(fibo(n))