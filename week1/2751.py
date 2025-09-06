import sys

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))

data.sort()

for item in data:
    sys.stdout.write(str(item) + '\n')