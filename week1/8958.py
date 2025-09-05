T = int(input())

for _ in range(T):
    point = 0
    answer = 0
    arr = list(input())
    for i in arr:
        if i == 'O':
            point += 1
        else:
            point = 0

        answer += point
    print(answer)