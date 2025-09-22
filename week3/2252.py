import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
check = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())

    graph[b].append(a)
    indegree[a] += 1

q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

answer = deque()
while q:

    cv = q.popleft()
    check[cv] = 1
    answer.appendleft(cv)

    for nv in graph[cv]:
        if check[nv] == 1: continue
        indegree[nv] -= 1
        if indegree[nv] == 0:
            q.append(nv)

print(*answer)



