import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

n = int(input())
m = int(input())

graph = {}

for _ in range(m):
    a, b = map(int, input().split())

    if a not in graph:
        graph[a] = []
    graph[a].append(b)

    if b not in graph:
        graph[b] = []
    graph[b].append(a)

def dfs(v, graph):
    count = 1

    for nv in graph.get(v, []):
        if visited[nv] == 0:
            visited[nv] = 1
            count += dfs(nv, graph)

    return count


visited = [0] * (n+1)
visited[1] = 1
print(dfs(1, graph) - 1)