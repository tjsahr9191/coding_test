a, b, v = map(int, input().split())

distancePerday = a - b
finalH = v - a

n = 0
if finalH % distancePerday != 0:
    print(finalH // distancePerday + 2)
else :
    print(finalH // distancePerday + 1)