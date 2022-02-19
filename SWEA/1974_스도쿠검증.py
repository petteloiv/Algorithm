import sys
sys.stdin=open("input.txt")

# -------------------trial 1 pass! ------------------------#
T = int(input())

for tc in range(1,T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # count 변수.. 틀린 값 나오면 1씩 더해줄 것 (왜냐면.. break 써도 안멈추는 문제 해결하지 못했다)
    count = 0

    # 3*3 배열 돌기
    for s in range(0, 9, 3):
        mini = []
        # 행 우선 순회 ..
        for i in range(s, s+3):
            # 열 변경
            for j in range(s, s+3):
                if sudoku[i][j] not in mini:
                    mini.append(sudoku[i][j])
                else:
                    count += 1
                    break

    # 행 우선 순회
    for i in range(9):
        row = []
        for j in range(9):
            if sudoku[i][j] not in row:
                row.append(sudoku[i][j])
            else:
                count += 1
                break

    # 열 우선 순회
    for j in range(9):
        column = []
        for i in range(9):
            if sudoku[i][j] not in column:
                column.append(sudoku[i][j])
            else:
                count += 1
                break

    # count가 0 이상이면 0 출력 .. 아니면 1 출력
    if count > 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')

