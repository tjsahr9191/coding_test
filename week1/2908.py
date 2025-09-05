def reverse(n):
    temp = n
    result = 0
    while(temp > 0):
        first = temp % 10
        result = result * 10 + first
        temp //= 10

    return result


a, b = map(int, input().split())

a = reverse(a)
b = reverse(b)


if a > b:
    print(a)
else :
    print(b)