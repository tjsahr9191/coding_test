n = int(input())

def hanoi(n, start, to, via):
    if n == 1:
        print(start, to)
        return

    hanoi(n-1, start, via, to)

    print(start, to)

    hanoi(n-1, via, to, start)

print(2**n - 1)

if n <= 20:
    hanoi(n, 1, 3, 2)