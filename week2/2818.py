from collections import deque
import sys

# 입력을 빠르게 받기 위해 input 함수를 재정의
input = sys.stdin.readline

q = deque()

n = int(input())
for _ in range(n):
    arr = list(input().split())

    command = arr[0]

    if command == 'push':
        q.append(arr[1])
    elif command == 'pop':
        if q: # len(q) > 0 보다 간결한 표현
            sys.stdout.write(q.popleft() + '\n')
        else:
            sys.stdout.write('-1\n')
    elif command == 'size':
        sys.stdout.write(str(len(q)) + '\n')
    elif command == 'empty':
        if not q: # len(q) == 0 보다 간결한 표현
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif command == 'front':
        if not q:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(q[0] + '\n')
    elif command == 'back':
        if not q:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(q[-1] + '\n')