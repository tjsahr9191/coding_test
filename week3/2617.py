import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

heavier_graph = [[] for _ in range(n + 1)]
lighter_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    heavier_graph[b].append(a)
    lighter_graph[a].append(b)

def dfs(v, graph, visited):
    visited[v] = True
    count = 0
    for nv in graph[v]:
        if not visited[nv]:
            count += 1 + dfs(nv, graph, visited)
    return count

heavier_counts = [0] * (n + 1)
lighter_counts = [0] * (n + 1)


for i in range(1, n + 1):
    visited_h = [False] * (n + 1)
    heavier_counts[i] = dfs(i, heavier_graph, visited_h)

    visited_l = [False] * (n + 1)
    lighter_counts[i] = dfs(i, lighter_graph, visited_l)

answer = 0
mid = (n + 1) // 2
for i in range(1, n + 1):
    if heavier_counts[i] >= mid or lighter_counts[i] >= mid:
        answer += 1

print(answer)