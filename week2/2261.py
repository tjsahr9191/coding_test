import sys
import heapq
import math
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()

def cal_dist(start, end, arr):
    min_dist = float('inf')

    for i in range(start, end + 1):
        for j in range(i + 1, end + 1):
            dist_sq = (arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2
            if dist_sq < min_dist:
                min_dist = dist_sq

    return min_dist

def cal_mid_dist(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

def recur(start, end, arr):

    size = end - start

    if size < 3:
        return cal_dist(start, end, arr)

    mid = (start + end) // 2

    left_min_dist = recur(start, mid, arr)
    right_min_dist = recur(mid + 1, end, arr)

    min_dist = min(left_min_dist, right_min_dist)

    divede_x = arr[mid][0]
    check_points = []
    for i in range(start, end):
        if (arr[i][0] - divede_x) ** 2 <= min_dist:
            check_points.append(arr[i])
    check_points.sort(key = lambda x : x[1])

    for i in range(len(check_points)):
        for j in range(i+1, len(check_points)):
            if (check_points[i][1] - check_points[j][1]) ** 2 >= min_dist:
                break

            min_dist = min(min_dist, cal_mid_dist(check_points[i], check_points[j]))

    return min_dist

print(recur(0, n-1, arr))
