arr = list(input())

stack = []
# -1 : delimiter, -2 : value
def delimiterToValue(ch):
    if ch == '(' or ch == ')':
        return 2
    if ch == '[' or ch == ']':
        return 3
    return 0

temp = []
def is_not_valid(arr):
    for ch in arr:
        if ch == '(' or ch == '[':
            temp.append(ch)
        else:
            if len(temp) <= 0:
                return True
            if delimiterToValue(ch) != delimiterToValue(temp[-1]):
                return True
            temp.pop()

    if len(temp) > 0:
        return True

    return False


if is_not_valid(arr):
    print(0)
    exit(0)

for ch in arr:
    if ch == '(' or ch == '[':
        stack.append((ch, -1))
    else:
        value = delimiterToValue(ch)
        inner_score = 0
        while len(stack) > 0 and stack[-1][1] == -2:
            inner_score += stack.pop()[0]
        inner_score *= value
        if inner_score == 0:
            inner_score = value
        stack.pop()
        stack.append((inner_score, -2))

sm = 0
for value, x in stack:
    sm += value
print(sm)


