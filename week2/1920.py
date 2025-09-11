n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()

def does_exist_in_binary_search(x):

    left = 0
    right = len(a)-1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            return True

        if a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return False

for x in b:
    if does_exist_in_binary_search(x):
        print(1)
    else:
        print(0)