import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
need = [[0] * (n+1) for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())

    graph[b].append([a, c])
    indegree[a] += 1

q = deque()
basic = []
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        need[i][i] = 1
        basic.append(i)

while q:

    v = q.popleft()

    for nv, k in graph[v]:

        for i in range(n+1):
            need[nv][i] += need[v][i] * k

        indegree[nv] -= 1
        if indegree[nv] == 0:
            q.append(nv)

basic.sort()

for x in basic:
    print(x, need[n][x])
