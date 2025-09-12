n, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

def cal_count(arr, distance):
    count = 1
    cur = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - cur >= distance:
            cur = arr[i]
            count += 1

    return count

lt = 1
rt = arr[-1] - arr[0]

answer = 0
while lt <= rt:
    mid = (lt + rt) // 2

    count = cal_count(arr, mid)

    if count >= c:
        answer = max(mid, answer)
        lt = mid + 1
    else:
        rt = mid - 1

print(answer)