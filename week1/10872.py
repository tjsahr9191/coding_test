n = int(input())

sumN = 1
for i in range(n, 1, -1):
    sumN = sumN * i

if n == 0:
    print(1)
else:
    print(sumN)