from collections import deque

n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
q = deque(arr)

answer = []

while q:
    for i in range(k-1):
        q.append(q.popleft())
    answer.append(q.popleft())

print('<', end = '')
print(', '.join(map(str, answer)), end = '')
print('>')