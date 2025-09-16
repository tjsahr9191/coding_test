import heapq
import sys
input = sys.stdin.readline

n = int(input())
circles = []

for _ in range(n):
    x, r = map(int, input().split())
    end = x + r
    dist = 2 * r
    circles.append((end, dist))

circles.sort()

h = []
count = 1
for end, dist in circles:
    start = end - dist
    last_point = end
    is_fill = False

    while h:
        e, d = heapq.heappop(h)
        e = -e

        if start >= e:
            heapq.heappush(h, (-e, d))
            break

        if e - d >= start and e != last_point:
            continue

        if e - d >= start:
            last_point = e - d

        if last_point == start:
            is_fill = True

    count += 1
    if is_fill:
        count += 1

    heapq.heappush(h, (-end, dist))

print(count)
