import sys
sys.stdin=open("14501.txt")

N = int(input())
# 걸리는 기간
ti = []
# 받을 수 있는 금액
pi = []
profit = [0] * (N+1)
sum = 0

# 1일 ~ N일까지 t, p 나눠서 저장하기
for i in range(N):
    t, p = map(int,input().split())
    ti.append(t)
    pi.append(p)

for i in range(N):
    # 합 .. 기존 합 , 기간 금액 중 큰 것
    sum = max(sum, profit[i])
    # 지금 날짜 + 걸리는 기간 이 N보다 크면 건너뛰기
    if i+ti[i] > N:
        continue
    profit[i+ti[i]] = max(sum+pi[i], profit[i + ti[i]])

print(max(profit))

