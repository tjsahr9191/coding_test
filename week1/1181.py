n = int(input())

arr = []
for _ in range(n):
    arr.append(input())

sorted_arr = sorted(arr, key = lambda x : (len(x), x))

cur_s = sorted_arr[0]
print(cur_s)
for idx in range(1, len(sorted_arr)):
    if sorted_arr[idx] == cur_s:
        continue
    print(sorted_arr[idx])
    cur_s = sorted_arr[idx]