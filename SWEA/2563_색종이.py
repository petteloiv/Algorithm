
N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]
# 100 * 100 의 빈 2차원 리스트 생성
blank = [[0]*101 for _ in range(101)]


for i in range(N):
    # 왼쪽 아래 (끝) 의 x,y 좌표
    x = numbers[i][0]
    y = numbers[i][1]

    # x, y 좌표를 기준으로 +10 (정사각형) 범위 설정
    for i in range(x, x+10):
        for j in range(y, y+10):
            # 2차원리스트 비어있을때만 +1 (겹친거 아예 날리기)
            if blank[i][j] == 0:
                blank[i][j] += 1

# 2차원 리스트의 값 중 1 있는 것만 세서 출력
count = 0
for i in range(1,101):
    for j in range(1,101):
        if blank[i][j] == 1:
            count += 1

print(count)