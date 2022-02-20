
T = 4
squares = [list(map(int,input().split())) for _ in range(4)]
# print(squares)

blank = [[0]*101 for _ in range(101)]

for t in range(4):
    # 각 좌표 변수에 저장
    x1 = squares[t][0]
    y1 = squares[t][1]
    x2 = squares[t][2]
    y2 = squares[t][3]

    # 왼쪽 ~ 오른쪽으로  범위 한정짓기
    for i in range(x1, x2):
        for j in range(y1, y2):
            # 범위 안의 값에 1 없을때만 1 더해주기
            # 겹치는 부분은 아예 안세겠다 ...
            if blank[i][j] == 0:
                blank[i][j] += 1
            else:
                continue

# blank에서 값이 1인 것 개수 세기기
count = 0
for i in range(1,101):
    for j in range(1,101):
        if blank[i][j] == 1:
            count += 1

print(count)