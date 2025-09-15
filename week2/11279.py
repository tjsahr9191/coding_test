import heapq
import sys

input = sys.stdin.readline

n = int(input())

max_heap = []

for _ in range(n):
    x = int(input())

    if x > 0:
        heapq.heappush(max_heap, -x)

    else:
        if max_heap:
            print(-heapq.heappop(max_heap))
        else:
            print(0)