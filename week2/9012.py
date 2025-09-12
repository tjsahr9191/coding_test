from collections import deque

n = int(input())

for _ in range(n):
    stack = deque()
    arr = list(input())
    flag = True
    for x in arr:
        if x == '(':
            stack.append(x)
        else:
            if len(stack) == 0:
                print('NO')
                flag = False
                break

            stack.pop()

    if flag:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')