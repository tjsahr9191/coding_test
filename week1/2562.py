maxV = -1
idx = -1

for i in range(1, 10):
    x = int(input())
    if x > maxV:
        maxV = x
        idx = i

print(maxV)
print(idx)