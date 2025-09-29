import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input().strip()) for _ in range(m)]
INF = float('inf')
dp = [[INF] * 152 for _ in range(n+1)]

if 2 in arr:
    print(-1)
    exit(0)

dp[2][1] = 1

for i in range(3, n+1):
    if i in arr: continue
    for j in range(1, min(i, 150)):
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1

if min(dp[n]) == INF:
    print(-1)
else:
    print(min(dp[n]))

