import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dist = [INF] * (n + 1)
for _ in range(m):
    a, b, w = map(int, input().split())

    graph[a].append([b, w])

start, end = map(int, input().split())

q = [[0, start]]
dist[start] = 0
while q:

    _w, node = heapq.heappop(q)

    if dist[node] < _w:
        continue

    for nxt, weight in graph[node]:
        if _w + weight < dist[nxt]:
            dist[nxt] = _w + weight
            heapq.heappush(q, [dist[nxt], nxt])

print(dist[end])