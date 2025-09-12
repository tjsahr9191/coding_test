from collections import deque

stack = deque()

k = int(input())

for _ in range(k):
    x = int(input())

    if x == 0:
        stack.pop()
    else:
        stack.append(x)

sm = 0
for x in stack:
    sm += x

print(sm)