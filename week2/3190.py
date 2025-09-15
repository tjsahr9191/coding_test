n = int(input())
k = int(input())
alst = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
blst = [list(input().split()) for _ in range(l)]

btbl = [0] * 10001
for time, dr in blst:
    btbl[int(time)] = dr

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

dr = 1
snake = [(1, 1)]
time = 0

while True:
    time += 1
    cy, cx = snake[0]
    ny = cy + dy[dr]
    nx = cx + dx[dr]

    if 1 <= ny <= n and 1 <= nx <= n and (ny, nx) not in snake:
        snake.insert(0, (ny, nx))
        if [ny, nx] in alst:
            alst.remove([ny, nx])
        else:
            snake.remove(snake[-1])

        if btbl[time] == 'D':
            dr = (dr + 1) % 4
        elif btbl[time] == 'L':
            dr = (dr + 3) % 4
    else:
        break

    # print(snake)

print(time)
