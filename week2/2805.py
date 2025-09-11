n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 1_000_000_000

answer = 0
while left <= right:
    h = (left + right) // 2

    sum_h = 0
    for i in range(n):
        sum_h += max(arr[i] - h, 0)

    if m == sum_h:
        answer = h
        break

    if sum_h > m:
        answer = max(answer, h)
        left = h+1
    else:
        right = h-1

print(answer)