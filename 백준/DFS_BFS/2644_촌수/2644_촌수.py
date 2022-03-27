
import sys
sys.stdin=open('input.txt')

# 전체 사람의 수
N = int(input())

# 계산해야하는 번호
S, E = map(int, input().split())

# 부모자식 관계 개수
M = int(input())

# 관계
lst = [list(map(int, input().split())) for _ in range(M)]

# print(lst)

# 필요한 리스트들 생성
arr = [[0] for _ in range(N+1)]
visited = [False] * (N+1)
chonsu = [0] * (N+1)

# queue
q = []


# 2차원 리스트에 부모자식 관계 집어넣기
for i in lst:
    arr[i[0]].append(i[1])
    arr[i[1]].append(i[0])


def Bfs(S):
    global q

    q.append(S)
    visited[S] = True

    while q:
        v = q.pop(0)
        for i in arr[v]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                chonsu[i] += (chonsu[v] + 1)

Bfs(S)

if chonsu[E] != 0:
    print(chonsu[E])
else:
    print(-1)