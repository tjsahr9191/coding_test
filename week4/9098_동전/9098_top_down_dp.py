import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def recur(idx, sm):

    if sm > amount:
        return 0
    if sm == amount:
        return 1
    if idx == n:
        return 0
    if dp[sm][idx] != 0:
        return dp[sm][idx]

    dp[sm][idx] = recur(idx, sm + coins[idx]) + recur(idx + 1, sm)

    return dp[sm][idx]

T = int(input())
for _ in range(T):
    n = int(input().strip())
    coins = list(map(int, input().split()))
    amount = int(input())

    coins.sort(reverse=True)

    dp = [[0] * n for _ in range(amount + 1)]

    answer = recur(0, 0)

    print(answer)