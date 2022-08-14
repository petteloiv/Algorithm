# n * m 직사각형 / 육지 or 바다 / 동서남북 중 한 곳 바라봄
# 맵의 각 칸 (A,B)
# A : 북쪽으로부터 떨어진 칸의 개수
# B : 서쪽으로부터 떨어진 칸의 개수
# 캐릭터 -> 상하좌우 이동 / 바다 못감 !
# 1. 현재 위치 : 현재방향 기준으로 왼쪽 (반시계 방향으로 90도 회전) 부터 차례대로 갈 곳
# 2. 바로 왼쪽 -> 안 가본 칸 존재 => 왼쪽 회전 & 왼쪽 + 1
# 3. 왼쪽에 안 가본 칸 X => 방향만 왼쪽 회전 & 1단계
# 4. 네 방향 모두 가봄 or 바다로 되어있는 칸 => 바라보는 방향 유지 & 뒤로 + 1 (뒤도 바다면 머무기)


n, m = map(int, input().split())

# 방향 d -> 북 0, 동 1, 남 2, 서 3
i, j, d = map(int, input().split())

# 육지, 바다 정보
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

# 방문 여부
visited = [[0]*m for _ in range(n)]

visited[i][j] = 1

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 왼쪽으로 돌기 (90도 회전 반시계 방향)

def left():
    global d
    d -= 1
    # 북 -> 서, 서-> 남, 남-> 동, 동->북
    if d == -1:
        d = 3

cnt = 1
turn = 0

while True:
    left()
    ni = i + di[d]
    nj = j + dj[d]

    # 안가본 칸 있으면 이동
    if visited[ni][nj] == 0 and arr[ni][nj] == 0:
        visited[ni][nj] = 1
        i = ni
        j = nj
        cnt += 1
        turn = 0
        continue
    else:
        # 회전하고 다시 1번으로
        turn += 1

    # 4번 돌았는데 갈 데 없는 경우
    if turn == 4:
        ni = i - di[d]
        nj = j - dj[d]

        # 뒤로 가능? 그럼 가셈
        if arr[ni][nj] == 0 :
            i = ni
            j = nj
        else:
            # 못가면 멈춰
            break
        turn = 0

print(cnt)
