n, m = map(int, input().split())

r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
flag = False
count = 0

def is_surround_clean(y, x):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == 0:
                return False

    return True

def dfs(y, x, d):
    global flag
    global count

    if flag:
        return

    if graph[y][x] == 0:
        graph[y][x] = 2
        count += 1

    if is_surround_clean(y, x):

        ny = y + dy[(d + 2) % 4]
        nx = x + dx[(d + 2) % 4]
        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == 0 or graph[ny][nx] == 2:
                dfs(ny, nx, d)
            else:
                flag = True
                return
    else:
        ny = y + dy[(d-1+4) % 4]
        nx = x + dx[(d-1+4) % 4]

        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == 0:
                dfs(ny, nx, (d-1+4) % 4)
            else:
                dfs(y, x, (d-1+4) % 4)

dfs(r, c, d)

print(count)