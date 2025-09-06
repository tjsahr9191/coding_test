def primeProcess(arr):
    size = len(arr)
    for idx in range(2, size):
        if arr[idx] == 0:
            for nx in range(2*idx, size, idx):
                arr[nx] = 1

T = int(input())

inputs = []

for _ in range(T):
    n = int(input())
    inputs.append(n)

maxNum = max(inputs)
primes = [0] * (maxNum+1)
primeProcess(primes)

for x in inputs:
    left = x // 2
    right = x // 2
    while left >= 0 and right <= x:
        if primes[left] == 0 and primes[right] == 0:
            if left + right == x:
                print(left, right)
                break
        left -= 1
        right += 1
