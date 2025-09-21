import sys
input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [0] * (n+1)
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)

def bfs(v):

    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        cv = q.popleft()

        for nv in graph[cv]:
            if visited[nv] == 0:
                visited[nv] = 1
                dist[nv] += dist[cv] + 1
                q.append(nv)

bfs(x)

result = []
for i in range(1, n+1):
    if dist[i] == k:
        result.append(i)

if result:
    result.sort()
    print(*result, sep = '\n')
else:
    print(-1)
