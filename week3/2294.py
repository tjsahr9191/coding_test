import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input().strip()) for _ in range(n)]
INF = float('inf')

dp = [INF] * (k+1)
dp[0] = 0

for amount in range(1, k+1):
    for c in coin:
        if amount - c >= 0:
            dp[amount] = min(dp[amount - c] + 1, dp[amount])

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])