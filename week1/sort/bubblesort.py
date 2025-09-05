inputs = [1, 6, 4, 3, 7, 8, 9]

n = len(inputs)

def bubblesort():
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if inputs[j] < inputs[j - 1]:
                inputs[j], inputs[j - 1] = inputs[j - 1], inputs[j]


def bubblesort_improve_1():
    for i in range(n - 1):
        exchange_count = 0
        for j in range(n - 1, i, -1):
            if inputs[j] < inputs[j - 1]:
                inputs[j], inputs[j - 1] = inputs[j - 1], inputs[j];
                exchange_count += 1

        if exchange_count == 0:
            break


def bubblesort_improve_2():
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            if inputs[j] < inputs[j - 1]:
                inputs[j], inputs[j - 1] = inputs[j - 1], inputs[j];
                last = j

        k = last


def double_direction_bubble_sort():
    left = 0
    right = n - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if inputs[j - 1] > inputs[j]:
                inputs[j - 1], inputs[j] = inputs[j], inputs[j - 1]
                last = j
        left = last

        for k in range(left, right):
            if inputs[k] > inputs[k + 1]:
                inputs[k], inputs[k + 1] = inputs[k + 1], inputs[k]
                last = k
        right = last

print(inputs)


