import sys

input = sys.stdin.readline

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]

meeting.sort(key = lambda x : (x[1], x[0]))

start = 0
end = 0
answer = 0
for i in range(n):
    if meeting[i][0] >= end:
        answer += 1
        start = meeting[i][0]
        end = meeting[i][1]

print(answer)