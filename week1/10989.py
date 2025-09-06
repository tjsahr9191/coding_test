import sys

n = int(sys.stdin.readline())

arr = [0] * 10001
for _ in range(n):
    idx = int(sys.stdin.readline())
    arr[idx] += 1

for i in range(1, len(arr)):
    if arr[i] == 0:
        continue

    for j in range(arr[i]):
        sys.stdout.write(str(i) + '\n')