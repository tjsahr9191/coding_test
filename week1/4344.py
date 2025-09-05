C = int(input())

for _ in range(C):
    data = list(map(int, input().split()))
    n = data[0]
    scores = data[1:]

    sum = 0
    for score in scores:
        sum += score
    avg = sum / n

    count = 0
    for score in scores:
        if score > avg:
            count += 1

    ratio = (count / n) * 100

    print(f'{ratio:.3f}%')