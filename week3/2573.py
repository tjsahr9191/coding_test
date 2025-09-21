import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(y, x):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if visited[ny][nx] == 0 and graph[ny][nx] != 0:
            visited[ny][nx] = 1
            dfs(ny, nx)

answer = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
while True:
    zero_counts = [[0] * m for _ in range(n)]
    answer += 1
    for y in range(1, n-1):
        for x in range(1, m-1):

            if graph[y][x] == 0:
                continue

            count = 0
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]

                if graph[ny][nx] == 0:
                    count += 1

            zero_counts[y][x] = count

    for y in range(1, n-1):
        for x in range(1, m-1):
            graph[y][x] = max(graph[y][x] - zero_counts[y][x], 0)

    visited = [[0] * m for _ in range(n)]
    island = 0
    no_ans_flag = True
    for y in range(1, n-1):
        for x in range(1, m-1):
            if graph[y][x] != 0 and visited[y][x] == 0:
                visited[y][x] = 1
                dfs(y, x)
                island += 1
                no_ans_flag = False

    if island >= 2:
        print(answer)
        break

    if no_ans_flag:
        print(0)
        break

