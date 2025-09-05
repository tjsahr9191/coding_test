T = int(input())

for _ in range(T):
    data = list(input().split())
    n = int(data[0])
    arr = [c for c in data[1]]

    for c in arr:
        for i in range(n):
            print(c, end='')
    print()