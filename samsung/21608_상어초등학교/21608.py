import sys

input = sys.stdin.readline;

n = int(input())
students_likes = {}
for _ in range(n*n):
    arr = list(map(int, input().split()))

    stud = arr[0]
    likes = arr[1:]

    students_likes[stud] = likes

graph = [[0] * n for _ in range(n)]
near_clean_count = [[-1] * n for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def find_place(stud):
    place = []
    likes = students_likes[stud]
    mx = -1
    for y in range(n):
        for x in range(n):
            if graph[y][x] != 0:
                continue

            likes_count = 0
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]

                if 0 <= ny < n and 0 <= nx < n:
                    if graph[ny][nx] in likes:
                        likes_count += 1

            if mx < likes_count:
                mx = likes_count
                place = [[y, x]]
            elif mx == likes_count:
                place.append([y, x])

    return place

def find_near_max_place(arr):
    place = []
    mx = -1
    for y, x in arr:
        count = 0
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] == 0:
                    count += 1

        if mx < count:
            mx = count
            place = [[y, x]]
        elif mx == count:
            place.append([ny, nx])

    return place

for stud in students_likes:

    find_place_cadidate = find_place(stud)

    final_y = 0
    final_x = 0
    if len(find_place_cadidate) > 1:
        find_near_max_place_candidate = find_near_max_place(find_place_cadidate)

        final_y = find_near_max_place_candidate[0][0]
        final_x = find_near_max_place_candidate[0][1]
    else:
        final_y = find_place_cadidate[0][0]
        final_x = find_place_cadidate[0][1]

    graph[final_y][final_x] = stud

def find_near_like_stud(y, x):
    stud = graph[i][j]
    likes = students_likes[stud]
    count = 0
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] in likes:
                count += 1

    return count

table = [0, 1, 10, 100, 1000]
answer = 0
for i in range(n):
    for j in range(n):
        count = find_near_like_stud(i, j)
        answer += table[count]

print(answer)

