n = int(input())

count = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[i] == row[x] or abs(i-x) == abs(row[i] - row[x]):
            return False
    return True

def n_queens(x):
    global count

    if x == n:
        count += 1
        return

    for i in range(n):
        row[x] = i
        if is_promising(x):
            n_queens(x+1)


n_queens(0)

print(count)