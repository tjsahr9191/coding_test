import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
answer = 0
def recur(length):
    global n, answer

    if length > n:
        return

    if length == n:
        answer += 1
        return

    recur(length + 2)
    recur(length + 1)

recur(0)
print(answer % 15746)