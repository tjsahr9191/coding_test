import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

n, m = map(int, input().split())

graph = {}
for _ in range(m):
    a, b = map(int, input().split())

    if a not in graph:
        graph[a] = []
    graph[a].append(b)

    if b not in graph:
        graph[b] = []
    graph[b].append(a)

def DFS(v, graph):

    for nv in graph.get(v, []):
        if visited[nv] == 0:
            visited[nv] = 1
            DFS(nv, graph)

visited = [0] * (n+1)
count = 0
for i in range(1, n+1):
    if visited[i] == 0:
        visited[i] = 1
        DFS(i, graph)
        count += 1

print(count)
