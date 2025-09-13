n = int(input())

arr = [int(input()) for _ in range(n)]

mx = arr[n-1]
count = 1
for i in range(n-1)[::-1]:
    if mx < arr[i]:
        count += 1
        mx = arr[i]

print(count)
