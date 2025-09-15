import sys
import heapq
input = sys.stdin.readline

n = int(input())

person = [list(map(int, input().split())) for _ in range(n)]

d = int(input())

valid_person = []
for start, end in person:
    if start > end:
        start, end = end, start

    if end - start <= d:
        valid_person.append((start, end))

valid_person.sort(key = lambda x : x[1])

heap = []

answer = 0
for start, end in valid_person:
    railway_start = end - d

    heapq.heappush(heap, start)

    while heap and heap[0] < railway_start:
        heapq.heappop(heap)

    answer = max(answer, len(heap))

print(answer)
