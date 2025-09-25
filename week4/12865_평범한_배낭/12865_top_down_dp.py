import sys

input = sys.stdin.readline

n, k = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n)]
def recur(idx, w):
    global k, answer

    if w > k:
        return -999999

    if idx == n:
        return 0

    if dp[idx][w] != 0:
        return dp[idx][w]

    dp[idx][w] = max(recur(idx+1, w + item[idx][0]) + item[idx][1], recur(idx+1, w))

    return dp[idx][w]

print(recur(0, 0))