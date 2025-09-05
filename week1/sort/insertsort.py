inputs = [1, 6, 4, 3, 7, 8, 9]

n = len(inputs)

for i in range(1, n):
    j = i
    temp = inputs[i]
    while j > 0 and inputs[j-1] > temp:
        inputs[j] = inputs[j-1]
        j -= 1
    inputs[j] = temp

print(inputs)