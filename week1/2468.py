from collections import deque

n = int(input())
graph = []
maxNum = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def bfs(row, col, h, visited):
    q = deque()
    q.append((row, col))
    visited[row][col] = 1

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == 0 and graph[ny][nx] > h:
                    visited[ny][nx] = 1
                    q.append((ny, nx))


result = 0
for i in range(maxNum):
    visited = [[0] * n for _ in range(n)]
    count = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                count += 1

    result = max(result, count)

print(result)