
import sys
sys.stdin=open('input.txt')

M, N, K = map(int, input().split())

arr = [[0]*N for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 사각형 해당 범위에 5 채워서 범위 표기
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 5

# 빈영역 넓이 저장할 리스트
result = []

# 전체 범위 돌면서
for i in range(M):
    for j in range(N):
        # 0인 경우 발견하면 ! count 1로 설정
        # queue에 저장
        # 값을 0 -> 1 로 변경 (처리해줬다는 표시)
        if arr[i][j] == 0:
            count = 1
            q = []
            q.append([i, j])
            arr[i][j] = 1

            # q 있는 동안
            while q:
                # 시작점 .. 뽑아쓰기
                y, x = q.pop(0)
                # 델타 돌면서 주변에 0 있는지 확인해야한다
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]

                    # 인접값이 범위 내 & 값이 0일 때!
                    if 0<=nx<N and 0<=ny<M and arr[ny][nx] == 0:
                        # 일단 값 1로 변경해서 처리
                        # q에 저장
                        # count += 1 (넓이에 추가)
                        arr[ny][nx] = 1
                        q.append([ny, nx])
                        count += 1

            # while문 끝나면 count에 저장된 넓이 result에 저장
            result.append(count)

result.sort()
cnt = len(result)

result = ' '.join(map(str, result))

print(cnt)
print(result)