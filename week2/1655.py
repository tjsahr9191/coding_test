import heapq
import sys

input = sys.stdin.readline

small = []
big = []

n = int(input())

for _ in range(n):
    x = int(input())

    if len(small) == len(big):
        heapq.heappush(small, -x)
    else:
        heapq.heappush(big, x)

    if small and big:
        left = -small[0]
        right = big[0]

        if left > right:
            heapq.heappop(small)
            heapq.heappop(big)
            heapq.heappush(small, -right)
            heapq.heappush(big, left)

    print(-small[0])