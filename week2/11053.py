n = int(input())

arr = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    mx = 0
    for j in range(i, -1, -1):
        if arr[i] > arr[j]:
            mx = max(mx, dp[j])

    dp[i] += mx

print(max(dp))