import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input().strip())
    coins = list(map(int, input().split()))
    amount = int(input())

    coins.sort()

    dp = [[0] * (n + 1) for _ in range(amount + 1)]

    for i in range(n + 1):
        dp[0][i] = 1

    for i in range(n - 1, -1, -1):
        for k in range(1, amount + 1):
            if k < coins[i]:
                dp[k][i] = dp[k][i+1]
            else:
                dp[k][i] = dp[k-coins[i]][i] + dp[k][i+1]

    print(dp[amount][0])