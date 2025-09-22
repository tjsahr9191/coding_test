import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

q1 = deque()
q2 = deque()
visited1 = [[0] * m for _ in range(n)]
visited2 = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            q1.append([i, j])
        if graph[i][j] == '*':
            q2.append([i, j])

L = 0
while q1 or q2:
    L += 1

    len1 = len(q1)
    for _ in range(len1):

        y, x = q1.popleft()
        if graph[y][x] == 'S' and visited1[y][x] == 1:
            graph[y][x] = '.'
        visited1[y][x] = 1


        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 'D' and graph[y][x] != '*':
                    print(L)
                    exit(0)
                if graph[ny][nx] == '.' and visited1[ny][nx] == 0:
                    visited1[y][x] = 1
                    graph[ny][nx] = 'S'
                    q1.append([ny, nx])

    len2 = len(q2)
    for _ in range(len2):

        y, x = q2.popleft()
        visited2[y][x] = 1

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 'S' and visited2[ny][nx] == 0:
                    visited2[ny][nx] = 1
                    graph[ny][nx] = '*'
                    q2.append([ny, nx])
                if graph[ny][nx] == '.' and visited2[ny][nx] == 0:
                    visited2[ny][nx] = 1
                    graph[ny][nx] = '*'
                    q2.append([ny, nx])
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'S':
                count += 1
    if count == 0:
        print('KAKTUS')
        break

