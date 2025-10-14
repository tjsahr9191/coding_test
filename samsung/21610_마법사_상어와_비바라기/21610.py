import sys

input = sys.stdin.readline

n, m = map(int, input().split())
buckets = [list(map(int, input().split())) for _ in range(n)]
clouds = [[[0, 0] for _ in range(n)] for _ in range(n)]
clouds[n-1][0] = [1, 1]
clouds[n-1][1] = [1, 1]
clouds[n-2][0] = [1, 1]
clouds[n-2][1] = [1, 1]
dr = [[], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

def add_water_in_buckets(y, x):
    buckets[y][x] += 1
    return

def clear_clouds(y, x):
    clouds[y][x][0] = 0
    return

def move_clouds(d, s):
    dy, dx = dr[d][0], dr[d][1]
    temp = []
    for y in range(n):
        for x in range(n):
            if clouds[y][x] == [1, 1]:
                ny = (y + dy * s) % n
                nx = (x + dx * s) % n
                temp.append([ny, nx])

                clouds[y][x] = [0, 0]

    for ny, nx in temp:
        clouds[ny][nx] = [1, 1]
        add_water_in_buckets(ny, nx)
        clear_clouds(ny, nx)

    water_bug(temp)

    return

def water_bug(arr):
    for y, x in arr:
        count = 0
        for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < n and 0 <= nx < n:
                if buckets[ny][nx] > 0:
                    count += 1

        buckets[y][x] += count

    return

def create_clouds():
    for y in range(n):
        for x in range(n):
            if buckets[y][x] >= 2 and clouds[y][x] != [0, 1]:
                clouds[y][x] = [1, 1]
                buckets[y][x] -= 2
    return

def reset_clouds():
    for i in range(n):
        for j in range(n):
            if clouds[i][j] == [0, 1]:
                clouds[i][j][1] = 0
    return

def sum_buckets():
    sm = 0
    for i in range(n):
        for j in range(n):
            sm += buckets[i][j]
    return sm

for _ in range(m):
    d, s = map(int, input().split())

    move_clouds(d, s)

    create_clouds()

    reset_clouds()

answer = sum_buckets()

print(answer)