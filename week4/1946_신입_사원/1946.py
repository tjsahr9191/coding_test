import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr.sort()
    mn = 100002
    answer = 0
    for a, b in arr:
        if b < mn:
            answer += 1
            mn = b

    print(answer)