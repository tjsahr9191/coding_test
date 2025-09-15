import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def is_white(y, x, n, graph):
    for i in range(n):
        for j in range(n):
            if graph[y+i][x+j] == 1:
                return False
    return True

def is_blue(y, x, n, graph):
    for i in range(n):
        for j in range(n):
            if graph[y+i][x+j] == 0:
                return False
    return True

def recur(y, x, n, graph):
    if is_white(y, x, n, graph):
        return 1, 0

    if is_blue(y, x, n, graph):
        return 0, 1

    mid = n // 2

    w1, b1 = recur(y, x, mid, graph)
    w2, b2 = recur(y, x + mid, mid, graph)
    w3, b3 = recur(y + mid, x, mid, graph)
    w4, b4 = recur(y + mid, x + mid, mid, graph)

    white = w1 + w2 + w3 + w4
    blue = b1 + b2 + b3 + b4

    return white, blue

answer = recur(0, 0, n, graph)
print(answer[0])
print(answer[1])


