m, n, l = map(int, input().split())
sadaes = list(map(int, input().split()))
sadaes.sort()

def find_closest_sadae_from(y):
    lt = 0
    rt = len(sadaes)-1

    optimal_result = 2_000_000_001
    optimal_pair = -1
    while lt <= rt:
        mid = (lt + rt) // 2

        if y == sadaes[mid]:
            return sadaes[mid]

        if optimal_result > abs(y - sadaes[mid]):
            optimal_pair = sadaes[mid]
            optimal_result = abs(y - sadaes[mid])

        if sadaes[mid] < y:
            lt = mid + 1
        else:
            rt = mid - 1

    return optimal_pair

count = 0
for _ in range(n):
    y, x = map(int, input().split())

    closest_sadae = find_closest_sadae_from(y)

    cal_L = abs(closest_sadae - y) + x

    if cal_L <= l:
        count += 1

print(count)