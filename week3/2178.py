import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, (input().strip()))) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = [[0] * (m) for _ in range(n)]

q = deque()
q.append([0, 0])
visited[0][0] = 1

while q:

    cy, cx = q.popleft()

    for k in range(4):
        ny = cy + dy[k]
        nx = cx + dx[k]

        if 0 <= ny < n and 0 <= nx < m:
            if visited[ny][nx] == 0 and graph[ny][nx] == 1:
                visited[ny][nx] = visited[cy][cx] + 1
                if ny == n-1 and nx == m-1:
                    print(visited[ny][nx])
                    break
                q.append([ny, nx])
