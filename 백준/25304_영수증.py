# 구매한 각 물건의 가격과 개수
# 구매한 물건들의 총 금액
# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 확인

# input
# X 영수증에 적힌 총 금액
# N 구매한 물건의 종류의 수
# a 물건의 가격 b 개수

# output
# 영수증에 적힌 금액과 일치하면 Yes 아니면 No 출력


price = int(input())
n = int(input())

receipt = 0

for i in range(n):
    p, c = map(int, input().split())
    receipt += p*c

if price == receipt:
    print('Yes')
else:
    print('No')