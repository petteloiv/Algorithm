
import sys
sys.stdin=open('input.txt')

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
distance = [[0]*M for _ in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

q = []

si = sj = 0
q.append([si, sj])
visited[si][sj] = True
distance[si][sj] = 1

while q:
    s = q.pop(0)
    si, sj = s[0], s[1]

    for d in range(4):
        ci = si + di[d]
        cj = sj + dj[d]

        if 0 <= ci < N and 0 <= cj < M and arr[ci][cj] == 1 and visited[ci][cj] == False:
            q.append([ci,cj])
            visited[ci][cj] = True
            distance[ci][cj] = distance[si][sj] + 1


print(distance[N-1][M-1])
