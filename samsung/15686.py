n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

chs = []
homes = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            homes.append((i, j))
        if graph[i][j] == 2:
            chs.append((i, j))

_min = 10000000
def recur(idx, ch):
    global _min

    if idx == len(chs):
        if len(ch) == m:
            total_min_dist = 0
            for home in homes:
                min_dist = 10000000
                for c in ch:
                    min_dist = min(abs(c[0] - home[0]) + abs(c[1] - home[1]), min_dist)
                total_min_dist += min_dist

            _min = min(_min, total_min_dist)
        return

    recur(idx+1, ch + [chs[idx]])
    recur(idx+1, ch)


ch = []
recur(0, ch)

print(_min)