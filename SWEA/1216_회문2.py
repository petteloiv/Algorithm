# question
# 회문 2 ~
# 회문 구해서 구할때마다 max_p < len(회문) 하면서 최대 길이 갱신시키기..
# 가로세로 모두 본다!
# 교수님 : 이때까지 가장 큰, 가장 작은 값 비교했다.
# 제일 큰 경우의 수 100...일거니까 큰 데이터부터 조사해서 비교하면 되겠죠
# 단일 알파벳 B 도 회문이다 ..

# -------------------문제 정의 ------------#
# 100*100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이 구하기
# 각 칸에 들어가는 글자 type = str / 'A', 'B', 'C' 중 하나
# 직선으로만 판단 !

# ----------- 알고리즘 풀이 ----------------#

import sys
sys.stdin=open("input.txt")

# 일단 회문을 함수로 만들기
def Palindrome(word):
    if word == word[::-1]:
        return 1


for t in range(10):
    tc = int(input())
    # 인풋받은 값 100*100 배열로 나열 ,, 프린트하는데 한세월 걸리네 ...
    p = [list(input()) for _ in range(100)]

    # 1. 행부터 찾기 .. row
    # 길이 100 부터 감소 ....
    # 회문 길이 최댓값 저장할 변수
    long_row = 0
    # m = 회문 길이 i = 열 j = 행
    for m in range(100,0,-1):
        for i in range(100):
            for j in range(100-m+1):
                find_row = []
                for k in range(m):
                    find_row.append(p[i][j+k])
                if Palindrome(find_row) == 1:
                    if long_row < len(find_row):
                        long_row = len(find_row)
                    break
                    # 이렇게 했는데 왜 ????????? 여기서 ????????? 안멈추고 큰값 -> 작은값 누적????????
                    # 비교 줘서 겨우.. 막음
                    # 왜 제일 큰 값에서 안멈추는가??????????????


    # 2. 열 찾기 column
    # 얘도 길이 100부터 감소
    # 회문 하나 나오면 저장하고 break
    # 열에서,, 회문길이 최댓값 저장
    long_col = 0
    # m = 회문 길이 i = 행 j = 열
    for m in range(100,0,-1):
        for i in range(100):
            for j in range(100-m+1):
                find_col = []
                for k in range(m):
                    find_col.append(p[j+k][i])
                if Palindrome(find_col) == 1:
                    if long_col < len(find_col):
                        long_col = len(find_col)
                    break

    # 비교해서 더 큰 숫자 출력
    if long_row > long_col:
        print(f'#{tc} {long_row}')
    else:
        print(f'#{tc} {long_col}')