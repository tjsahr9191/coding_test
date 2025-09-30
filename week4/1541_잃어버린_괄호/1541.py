import sys

input = sys.stdin.readline

s = input().strip()
arr = s.split('-')
result = []
for v in arr:
    sm = 0
    temp = v.split('+')
    for e in temp:
        sm += int(e)
    result.append(sm)

answer = result[0]
for i in range(1, len(result)):
    answer -= result[i]

print(answer)
