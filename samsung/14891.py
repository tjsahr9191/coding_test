# 맞닿아 있는 부분이 다르면 회전
# N극 : 0, S극 : 1
# 방향 1 : 시계, -1 : 반시계
n = 4
wheels = [list(int(i) for i in input()) for _ in range(n)]

k = int(input())
rotates = [list(map(int, input().split())) for _ in range(k)]
for rotate in rotates:
    rotate[0] -= 1

def rotate(idx, dr):
    wheel = wheels[idx]
    if dr == 1:
        last = wheel.pop()
        wheel.insert(0, last)
    else:
        first = wheel.pop(0)
        wheel.append(first)

def check_pole(idx):
    left_pole = []
    left_idx = idx
    while left_idx > 0:
        cur_wheel = wheels[left_idx]
        left_wheel = wheels[left_idx-1]
        left_pole.append(cur_wheel[6] != left_wheel[2])
        left_idx -= 1

    right_pole = []
    right_idx = idx
    while right_idx < n-1:
        cur_wheel = wheels[right_idx]
        right_wheel = wheels[right_idx+1]
        right_pole.append(cur_wheel[2] != right_wheel[6])
        right_idx += 1

    return left_pole, right_pole

def sum_of_score():
    _sum = 0
    for i in range(n):
        pole = wheels[i][0]

        if pole == 1:
            _sum += 1 << i

    return _sum

for i in range(k):
    idx, dr = rotates[i]

    left_pole, right_pole = check_pole(idx)

    for j in range(len(left_pole)):
        if not left_pole[j]:
            break

        if j % 2 == 0:
            rotate(idx-1-j, -dr)
        else:
            rotate(idx-1-j, dr)

    for j in range(len(right_pole)):
        if not right_pole[j]:
            break

        if j % 2 == 1:
            rotate(idx+1+j, dr)
        else:
            rotate(idx+1+j, -dr)

    rotate(idx, dr)

print(sum_of_score())

