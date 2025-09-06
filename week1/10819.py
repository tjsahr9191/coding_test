n = int(input());
arr = list(map(int, input().split()))

def recur(idx):
    global result
    global arr
    global maxV
    global pm

    if idx == len(result):
        maxV = max(maxV, cal(result))

    for i in range(len(arr)):
        if pm[i] == 0:
            pm[i] = 1
            result.append(arr[i])
            recur(idx+1)
            result.pop()
            pm[i] = 0

def cal(arr):
    sumV = 0
    for i in range(1, len(arr)):
        sumV += abs(arr[i-1] - arr[i])
    return sumV

maxV = -1
result = []
pm = [0] * n
recur(0)

print(maxV)