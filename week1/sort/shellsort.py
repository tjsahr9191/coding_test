a = [1, 6, 4, 3, 7, 8, 9]

n = len(a)

h = n // 2
while h > 0:
    for i in range(h, n):
        j = i - h
        temp = a[i]
        while j >= 0 and a[j] > temp:
            a[j+h] = a[j]
            j -= h

        a[j+h] = temp
    h //= 2

print(a)