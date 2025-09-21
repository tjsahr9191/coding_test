import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
days = [[[0] * m for _ in range(n)] for _ in range(h)]

dy = [-1, 0, 1, 0, 0, 0]
dx = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()
# 1 : 익은 토마토, 0 : 안익은 토마토, -1 : 토마토 없음

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                q.append([k, i, j])

while q:

    cz, cy, cx = q.popleft()

    for k in range(6):
        nz = cz + dz[k]
        ny = cy + dy[k]
        nx = cx + dx[k]

        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
            if graph[nz][ny][nx] == -1:
                continue

            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = 1
                days[nz][ny][nx] = days[cz][cy][cx] + 1
                q.append([nz, ny, nx])

answer = -1
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                print(-1)
                exit(0)

            answer = max(days[k][i][j], answer)

print(answer)
