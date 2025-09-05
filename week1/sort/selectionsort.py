inputs = [1, 6, 4, 3, 7, 8, 9]

n = len(inputs)

for i in range(n-1):
    min = i
    for j in range(i+1, n):
        if inputs[j] < inputs[min]:
            min = j
    inputs[min], inputs[i] = inputs[i], inputs[min]

print(inputs)