import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

def power(a, b, c):
    if b == 1:
        return a % c

    val = power(a, b // 2, c)

    val = (val * val) % c

    if b % 2 == 1:
        val = (val * a) % c

    return val

print(power(A, B, C))