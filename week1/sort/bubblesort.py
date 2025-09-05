inputs = [1, 6, 4, 3, 7, 8, 9]

n = len(inputs)
for i in range(n-1):
    for j in range(n-1, i, -1):
        if inputs[j] < inputs[j-1]:
            inputs[j], inputs[j-1] = inputs[j-1], inputs[j];

print(inputs)