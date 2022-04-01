
import sys
sys.stdin=open('input.txt')

N = int(input())

# 연결된 노드들 입력해줄 배열 ..
arr = [[] for _ in range(N+1)]

# n번 노드 방문 직전 노드 .. 직접 연결 노드? 표시용
visited = [0] * (N+1)

# 입력받은값들 집어넣기
# 연결된 두 정점 입력!
for i in range(N-1):
    n1, n2 = map(int,input().split())

    arr[n1].append(n2)
    arr[n2].append(n1)

# 연결된 노드들 중에서 방문 안한 노드 확인 ;
# 있다면 부모노드에 지금값 저장해두고
# 또 연결해서 ... 찾으러 들어간다
def Dfs(s):
    for i in arr[s]:
        if visited[i] == 0:
            visited[i] = s
            Dfs(i)

# 1로 시작하라고했다..
Dfs(1)

# 2번부터 출력하라며,,
for i in range(2, N+1):
    print(visited[i])