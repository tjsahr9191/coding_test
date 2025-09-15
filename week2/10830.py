import sys
input = sys.stdin.readline

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def multiple(mat1, mat2):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += mat1[i][k] * mat2[k][j]
            res[i][j] %= 1000
    return res

def recur(arr, b):

    if b == 1:
        for i in range(n):
            for j in range(n):
                arr[i][j] %= 1000
        return arr

    sub_matrix = recur(arr, b // 2)

    mul_matrix = multiple(sub_matrix, sub_matrix)


    if b % 2 == 1:
        mul_matrix = multiple(mul_matrix, arr)

    return mul_matrix

answer = recur(arr, b)

for row in answer:
    print(*row)
