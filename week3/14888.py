import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
opers = list(map(int, input().split()))
ans_min = 100 ** 10 + 1
ans_max = -100 ** 10 - 1

def recur(idx, sm, add, sub, mul, div):
    global ans_min, ans_max

    if idx == n:
        ans_min = min(ans_min, sm)
        ans_max = max(ans_max, sm)
        return

    if add > 0:
        recur(idx+1, sm + arr[idx], add-1, sub, mul, div)
    if sub > 0:
        recur(idx+1, sm - arr[idx], add, sub-1, mul, div)
    if mul > 0:
        recur(idx+1, sm * arr[idx], add, sub, mul-1, div)
    if div > 0:
        recur(idx+1, int(sm / arr[idx]), add, sub, mul, div-1)

recur(1, arr[0], opers[0], opers[1], opers[2], opers[3])

print(ans_max)
print(ans_min)