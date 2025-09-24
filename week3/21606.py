import sys

sys.setrecursionlimit(200005)
input = sys.stdin.readline

n = int(input())

place = [0] + list(map(int, input().strip()))
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    count = 0
    for next_node in graph[v]:
        if place[next_node] == 1:
            count += 1
        elif visited[next_node] == 0:
            visited[next_node] = 1
            count += dfs(next_node)
    return count

ans = 0
for i in range(1, n+1):
    if place[i] == 0:
        if visited[i] == 0:
            visited[i] = 1
            res = dfs(i)
            ans += res * (res - 1)

    else:
        for next_node in graph[i]:
            if place[next_node] == 1:
                ans += 1

print(ans)