from collections import deque
# 악 시간초과! 시간초과!
import sys
input = sys.stdin.readline

# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())

# 도시 / 최단거리
graph = [[] for _ in range(n+1)]
# 최단거리 -1로 설정 / 출발 도시는 0으루~
dist = [-1] * (n+1)
dist[x] = 0

# m개 줄에 걸쳐서 a,b
# a -> b 이동하는 도로 있음!
# 도로 정보 입력하기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# bfs
# 출발 도시부터 ~ 시작~~
queue = deque([x])
while queue:
    city = queue.popleft()
    # 이동 가능한 도시 확인
    for i in graph[city]:
        # 방문 X 도시 => 거리가 -1이다 
        if dist[i] == -1:
            dist[i] = dist[city] + 1
            queue.append(i)


ans = False
# for 문 돌면서 최단거리 있다면 출력
# 있으면 ans True로 변경
for j in range(1, n+1):
    if dist[j] == k:
        print(j)
        ans = True

# 없으면 -1 출력
if ans == False:
    print(-1)