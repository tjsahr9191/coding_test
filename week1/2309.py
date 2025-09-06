arr = []
for _ in range(9):
    arr.append(int(input()))

def recur(idx, total, lists):
    global arr
    global flag

    if flag:
        return

    if total > 100:
        return

    if len(lists) == 7:
        if total == 100:
            flag = True
            lists.sort()
            for x in lists:
                print(x)
        return

    if idx >= len(arr):
        return

    recur(idx+1, total + arr[idx], lists + [arr[idx]])
    recur(idx+1, total, lists)
flag = False
result = []
recur(0, 0, result)