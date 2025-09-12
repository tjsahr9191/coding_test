n = int(input())
operates = [list(input().split()) for _ in range(n)]
stack = [0] * 10000
head = 0

for oper in operates:
    if oper[0] == 'top':
        if head == 0:
            print(-1)
        else:
            print(stack[head-1])
    elif oper[0] == 'pop':
        if head == 0:
            print(-1)
        else:
            head -= 1
            print(stack[head])

    elif oper[0] == 'size':
        print(head)
    elif oper[0] == 'empty':
        if head == 0:
            print(1)
        else:
            print(0)
    elif oper[0] == 'push':
        v = int(oper[1])
        stack[head] = v
        head += 1