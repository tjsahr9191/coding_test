import sys

input = sys.stdin.readline

n, k = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(n)]

def recur(idx, w, v):
    global k, answer

    if idx == n:
        if w <= k:
            answer = max(answer, v)
        return

    recur(idx+1, w + item[idx][0], v + item[idx][1])
    recur(idx+1, w, v)

answer = -1
recur(0, 0, 0)

print(answer)