def isPrime(num):
    if num == 1:
        return False

    for x in range(2, num//2+1):
        if num % x == 0:
            return False

    return True


n = int(input())
arr = list(map(int, input().split()))

count = 0
for i in arr:
    if isPrime(i):
        count += 1

print(count)