import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = {}
for _ in range(n-1):
    a, b = map(int, input().split())

    if a not in graph:
        graph[a] = []
    graph[a].append(b)

    if b not in graph:
        graph[b] = []
    graph[b].append(a)

par = [0] * (n+1)
visited = [0] * (n+1)
def dfs(v, graph):

    for nv in graph.get(v, []):
        if visited[nv] == 0:
            visited[nv] = 1
            par[nv] = v
            dfs(nv, graph)

visited[1] = 1
dfs(1, graph)

print(*par[2:], sep = '\n')

