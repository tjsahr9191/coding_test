x, y = map(int, input().split())
n = int(input())

rows = [0, y]
cols = [0, x]
for _ in range(n):
    direction, v = map(int, input().split())
    if direction == 0:
        rows.append(v)
    else:
        cols.append(v)

rows.sort()
cols.sort()

calRows = []
calCols = []
for idx in range(1, len(rows)):
    calRows.append(rows[idx] - rows[idx-1])
for idx in range(1, len(cols)):
    calCols.append(cols[idx] - cols[idx-1])

maxV = -1
for y in calCols:
    for x in calRows:
        maxV = max(maxV, y*x)

print(maxV)
