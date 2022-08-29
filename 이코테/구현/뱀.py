# N * N 정사각 보드
# 몇몇칸 사과 / 상하좌우 끝 == 벽
# 게임 시작 : 뱀 (맨 위 맨 좌측 위치, 길이 1, 오른쪽 향함)
# 뱀뱀이 이동규칙 !
# 머리 다음칸 / 이동한 칸에 사과 있으면 -> 사과 없어지고 꼬리 이동 x
# 이동한 칸에 사과 없으면 -> 몸길이 줄여서 꼬리가 위치한 칸 비워줌 / 몸길이 변화 x
# 게임이 몇 초에 끝나는지!
# 뱀뱀이가 벽 / 자기 자신의 몸과 부딪히면 게임 끗~!
# 이거 분명 어디선가 풀었는데

# 보드
n = int(input())
board = [[0] * n for _ in range(n)]  # empty : 0

# 사과 위치
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 2

# 방향
l = int(input())
times = [0] * 10000
for _ in range(l):
    t, d = input().split()
    times[int(t)] = d

# 뱀뱀이 위치 1
snake = []
snake.append([0, 0])
board[0][0] = 1

# 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d = 1
# 시작 위치
nx, ny = 0, 0

time = 0

while (True):
    time += 1
    nx = nx + dx[d]
    ny = ny + dy[d]

    # 벽이나 몸에 닿으면
    if (nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1):
        break

    # yes 사과
    if (board[nx][ny] == 2):
        snake.append([nx, ny])
        board[nx][ny] = 1

    # no 사과
    elif (board[nx][ny] == 0):
        snake.append([nx, ny])
        board[nx][ny] = 1

        sx, sy = snake.pop(0)
        board[sx][sy] = 0

    # 방향 바꿀 시간인가요?
    if (times[time] == 'D'):
        d = (d + 1) % 4
    elif (times[time] == 'L'):
        d = (d + 3) % 4

print(time)