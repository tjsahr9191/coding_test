x, y, w, h = map(int, input().split())

minX = min(x, w-x)
minY = min(y, h-y)

print(min(minX, minY))