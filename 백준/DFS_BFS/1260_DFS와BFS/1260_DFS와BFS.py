import sys
sys.stdin=open('input.txt')


N, M, V = map(int, input().split())
basic = [list(map(int,input().split())) for _ in range(M)]

# 2차원 배열 ; 출발 종료 저장할 .. array 만들기
arr = [[0] * (N+1) for _ in range(N+1)]
# print(arr)

# 순서 없으니까 양 쪽 다 넣어주기
for i in basic:
    arr[i[0]][i[1]] = arr[i[1]][i[0]] = 1

visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

bfs = []
dfs = []

def Bfs(v):
    queue = []

    queue.append(v)
    visited1[v] = True

    while queue:
        v = queue.pop(0)
        bfs.append(v)

        for i in range(1, N+1):
            # 방문 안했고! 연결되는 노드가 있는 경우
            if visited1[i] == False and arr[v][i] == 1:
                queue.append(i)
                visited1[i] = True



def Dfs(v):
    visited2[v] = True
    dfs.append(v)

    for i in range(1, N+1):
        if visited2[i] == False and arr[v][i] == 1:
            Dfs(i)


Dfs(V)
Bfs(V)


dfs = ' '.join(map(str, dfs))
bfs = ' '.join(map(str, bfs))

print(dfs)
print(bfs)