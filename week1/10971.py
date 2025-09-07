n = int(input())

w = []
for _ in range(n):
    w.append(list(map(int, input().split())))

visited = [False] * n

answer = 10000000
def recur(first, cur, count, sum_val):
    global answer

    if count == n:
        if w[cur][first] != 0:
            answer = min(answer, sum_val + w[cur][first])
        return

    for next_node in range(n):
        if w[cur][next_node] != 0 and not visited[next_node]:
            visited[next_node] = True
            recur(first, next_node, count + 1, sum_val + w[cur][next_node])
            visited[next_node] = False


for i in range(n):
    visited[i] = True
    recur(i, i, 1, 0)
    visited[i] = False

print(answer)
