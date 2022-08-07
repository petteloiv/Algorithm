# 0과 1로만 이루어진 문자열 S
# 모든 숫자 같게 만들기 ~ ex) 00000 11111
# 연속된 하나 이상의 숫자 잡고 뒤집기 가능 : 0 <-> 1

# 1. 문자열 첫번째 숫자 확인
# 2. for문 돌면서 현재 값 - 다음 값 확인
# 두 개가 다를 때만 변경 횟수 올려준다.
# 바뀌는 횟수 더 적은 것 == 행동의 최소 횟수

num = list(map(int, input()))

to0 = 0
to1 = 0

if num[0] == 1:
    to0 += 1
else:
    to1 += 1

for i in range(len(num)-1):
    if num[i] != num[i+1]:
        if num[i+1] == 1:
            to0 += 1
        else:
            to1 += 1

if to0 > to1:
    print(to1)
else:
    print(to0)

