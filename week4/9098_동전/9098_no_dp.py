import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def recur(index, sm):
    if sm > amount:
        return 0
    if sm == amount:
        return 1
    if index == n:
        return 0

    use_it = recur(index, sm + coins[index])
    dont_use_it = recur(index + 1, sm)

    return use_it + dont_use_it

T = int(input())
for _ in range(T):
    n = int(input().strip())
    coins = list(map(int, input().split()))
    amount = int(input())

    coins.sort(reverse=True)

    result = recur(0, 0)
    print(result)