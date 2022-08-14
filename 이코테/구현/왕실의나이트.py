# 8*8 좌표평면 -> 특정 한 칸에 나이트
# L자 형태 이동
# 1) 수평 +2 수직 +1
# 2) 수직 +2 수평 +1
# 행 : 1~8 열 : a~h
# 벗어나기 금지!
# 나이트 위치 주어졌을 때 이동할 수 있는 경우의 수

# input: 열행 ex) a1

# ------------------------------
# 현재 위치 + 이동경로 => 8*8 안에 있는지 확인

knightnow = input()
i = int(knightnow[1])
j = int(ord(knightnow[0])) - int(ord('a')) +1

# 이동할 수 있는 모든 가능성

di = [-2, -1, 1, 2, 2, 1, -1, -2]
dj = [-1, -2, -2, -1, 1, 2, 2, 1]

cnt = 0

for d in range(len(di)):
    ni = i + di[d]
    nj = j + dj[d]
    if 1 <= ni <= 8 and 1 <= nj <= 8:
        cnt += 1


print(cnt)
