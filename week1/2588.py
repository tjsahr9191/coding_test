a = int(input())
b = int(input())

f = a * (b % 10)
b //= 10
s = a * (b % 10)
b //= 10
t = a * (b % 10)

print(f)
print(s)
print(t)
print(t * 100 + s * 10 + f)