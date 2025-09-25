import sys

input = sys.stdin.readline

n, k = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]

for idx in range(1, n+1):
    weight, value = item[idx-1]
    for w in range(1, k+1):
        if w < weight:
            dp[idx][w] = dp[idx-1][w]
        else:
            dp[idx][w] = max(dp[idx-1][w - weight] + value, dp[idx-1][w])

print(dp[n][k])

