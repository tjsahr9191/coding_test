n = int(input())
arr = list(map(int, input().split()))
arr.sort()

min_sum = 2_000_000_000

f_lt = -1
f_rt = -1
for i in range(n):
    lt = i+1
    rt = n-1
    while lt <= rt:
        mid = (lt + rt) // 2

        result = arr[i] + arr[mid]
        if result == 0:
            print(arr[i], arr[mid])
            exit(0)

        if abs(result) < min_sum:
            f_lt = i
            f_rt = mid
            min_sum = abs(result)

        if result < 0:
            lt = mid + 1
        else:
            rt = mid - 1

print(arr[f_lt], arr[f_rt])


