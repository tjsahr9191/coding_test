import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input().strip()) for _ in range(n)]
arr.sort(reverse=True)

answer = 0
for i in range(n):
    if arr[i] <= k:
        answer += (k//arr[i])
        k = k % arr[i]

print(answer)