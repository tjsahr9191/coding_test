n = int(input())

count = 0
for i in range(1, n+1):
    if i // 100 == 0:
        count += 1
    else:
        arr = [int(digit) for digit in str(i)]
        gap = arr[1] - arr[0]
        for j in range(1, len(arr)-1):
            sub = arr[j+1] - arr[j]
            if gap != sub:
                continue
            count += 1

print(count)