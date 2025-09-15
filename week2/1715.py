import sys
import heapq

input = sys.stdin.readline

n = int(input())
decks = [int(input()) for _ in range(n)]

heapq.heapify(decks)

answer = 0
while len(decks) > 1:
    first = heapq.heappop(decks)
    second = heapq.heappop(decks)
    answer += first + second
    heapq.heappush(decks, first+second)

print(answer)