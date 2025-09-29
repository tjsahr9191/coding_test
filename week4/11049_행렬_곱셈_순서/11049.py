import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
mat = [[]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (n+1) for _ in range(n+1)]

def recur(s, e):
    if dp[s][e] != -1:
        return dp[s][e]
    if s == e:
        return 0
    if s+1 == e:
        dp[s][e] = mat[s][0] * mat[s][1] * mat[e][1]
        return dp[s][e]

    result = 1 << 31
    for i in range(s, e):
        result = min(result, recur(s, i) + recur(i+1, e) + mat[s][0] * mat[i][1] * mat[e][1])

    dp[s][e] = result

    return dp[s][e]

print(recur(1, n))