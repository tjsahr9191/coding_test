import sys
input = sys.stdin.readline

v, e = map(int, input().split())

edges = []
par = [i for i in range(v+1)]
rank = [0 for _ in range(v+1)]

def _union(a, b):
    a = _find(a)
    b = _find(b)

    if rank[a] < rank[b]:
        par[a] = b
    elif rank[b] < rank[a]:
        par[b] = a
    else:
        par[b] = a
        rank[a] += 1

def _find(x):
    while x != par[x]:
        x = par[x]

    return x

for _ in range(e):
    a, b, c = map(int, input().split())

    edges.append([a, b, c])

edges.sort(key = lambda x : x[2])

answer = 0
for a, b, w in edges:

    if _find(a) == _find(b):
        continue

    _union(a, b)
    answer += w

print(answer)