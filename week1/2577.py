a = int(input())
b = int(input())
c = int(input())

value = a * b * c
s = str(value)

arr = [int(digit) for digit in s]
result = [0] * 10
for x in arr:
    result[x] += 1

for x in result:
    print(x)