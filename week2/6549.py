import sys
input = sys.stdin.readline

answer = []

def recur(histogram, start, end):

    if start == end:
        return histogram[end]
    elif start + 1 == end:
        if histogram[start] > histogram[end]:
            return max(histogram[start], histogram[end] * 2)
        return max(histogram[end], histogram[start] * 2)

    mid = (start + end) // 2

    left_area = recur(histogram, start, mid)
    right_area = recur(histogram, mid + 1, end)

    mid_area = histogram[mid]
    cur_h = histogram[mid]
    right = mid + 1
    left = mid - 1

    while start <= left <= end and start <= right <= end:
        if histogram[right] < histogram[left]:
            if histogram[left] < cur_h:
                cur_h = histogram[left]
            mid_area = max(mid_area, cur_h * (right - left))
            left -= 1
        else:
            if histogram[right] < cur_h:
                cur_h = histogram[right]
            mid_area = max(mid_area, cur_h * (right - left))
            right += 1

    while start <= left <= end:
        if histogram[left] < cur_h:
            cur_h = histogram[left]
        mid_area = max(mid_area, cur_h * (right - left))
        left -= 1

    while start <= right <= end:
        if histogram[right] < cur_h:
            cur_h = histogram[right]
        mid_area = max(mid_area, cur_h * (right - left))
        right += 1

    return max(left_area, mid_area, right_area)


while True:
    histogram = list(map(int, input().split()))

    if histogram[0] == 0: break

    n = histogram[0]

    answer.append(recur(histogram, 1, n))

for x in answer:
    print(x)

