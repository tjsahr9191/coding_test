import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

_max = -1_000_000_001
_min = 1_000_000_001

def recur(idx, value, add, sub, mul, div):
    global _max, _min

    if idx == n:
        _max = max(value, _max)
        _min = min(value, _min)
        return

    if add > 0:
        recur(idx+1, value + a[idx], add-1, sub, mul, div)
    if sub > 0:
        recur(idx+1, value - a[idx], add, sub-1, mul, div)
    if mul > 0:
        recur(idx+1, value * a[idx], add, sub, mul-1, div)
    if div > 0:
        result = int(value / a[idx])
        recur(idx+1, result, add, sub, mul, div-1)

recur(1, a[0], add, sub, mul, div)

print(_max)
print(_min)
