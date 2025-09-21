import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
INF = float('inf')
graph = [list(map(int, input().strip())) for _ in range(n)]
counts = [[INF] * (n) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

q = deque()
q.append([0, 0])
counts[0][0] = 0

while q:

    y, x = q.popleft()

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] == 0:
                if counts[y][x] + 1 < counts[ny][nx]:
                    counts[ny][nx] = counts[y][x] + 1
                    q.append([ny, nx])
            else:
                if counts[y][x] < counts[ny][nx]:
                    counts[ny][nx] = counts[y][x]
                    q.appendleft([ny, nx])

print(counts[n-1][n-1])