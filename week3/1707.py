import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

k = int(input())

def dfs(v, check):
    global graph, visited

    for nv in graph[v]:
        if visited[nv] == 0:
            visited[nv] = -check
            dfs(nv, -check)

for _ in range(k):
    flag = False
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        u, v = map(int, input().split())

        graph[u].append(v)
        graph[v].append(u)


    for i in range(1, V+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, 1)

    for i in range(1, len(graph)):
        for j in graph[i]:
            if visited[i] == visited[j]:
                flag = True
                break
        if flag:
            break

    if flag:
        print('NO')
    else:
        print('YES')

