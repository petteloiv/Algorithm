
import sys
sys.stdin=open('input.txt')

# 컴퓨터의 수
N = int(input())

# 연결된 쌍
M = int(input())

# 연결된 애들 받아오기
lst = [list(map(int, input().split())) for _ in range(M)]

# 2차원 배열
arr = [[0] * (N+1) for _ in range(N+1)]

for i in lst:
    arr[i[0]][i[1]] = arr[i[1]][i[0]] = 1

# 전파된 바이러스 컴퓨터 셀 변수
cnt = 0

# 방문 여부
visited = [False] * (N+1)

def Dfs(v):
    global cnt

    visited[v] = True
    cnt += 1

    for i in range(1, N+1):
        if arr[v][i] == 1 and visited[i] == False:
            Dfs(i)

Dfs(1)
print(cnt-1)