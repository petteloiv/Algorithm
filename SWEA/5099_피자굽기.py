# ----------문제 정의 ----------#
# 피자 빼고 다시 넣으면서 치즈 양 확인 -> 치즈 줄이기
# 피자와 순서 같이 이동
# result에 나온 순서대로 덮어쓰기

# ---------------알고리즘 풀이 -----------------#
import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    num = []
    for i in range(1,M+1):
        num.append(i)
    result = 0

    while pizza:
       # 1번 위치 피자 확인
       now = pizza[0]
       # 치즈 다 녹아서 0 이면 빼기
       if now == 0:
           pizza.pop(0)
           result = num.pop(0)
           continue
       # 치즈가 0이 아니면
       else:
           # 치즈 반절로 줄여서 다시 넣기
           # 피자 번호도 같이 뺐다가 다시 넣기
           now = pizza.pop(0)//2
           nownum = num.pop(0)
           pizza.append(now)
           num.append(nownum)

    print(f'#{tc} {result}')

# ---------- case 3번 틀림 ----------#
# 왜,, 틀렸을까..? 뭐가 문제야야