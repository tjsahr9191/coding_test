n, r, c = map(int, input().split())

count = 0
def recur(n, r, c):
    global count

    boardSize = 1 << n
    mid = boardSize // 2

    if n == 0:
        return

    if r < mid and c < mid:
        recur(n-1, r, c)
    elif r < mid and c >= mid:
        count += mid * mid
        recur(n-1, r, c-mid)
    elif r >= mid and c < mid:
        count += 2 * mid * mid
        recur(n-1, r-mid, c)
    else:
        count += 3 * mid * mid
        recur(n-1, r-mid, c-mid)

recur(n, r, c)

print(count)