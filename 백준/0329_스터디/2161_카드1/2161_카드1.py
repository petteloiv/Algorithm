import sys
sys.stdin=open('input.txt')


N = int(input())

# 카드 순서대로 입력해 줄 리스트
card = []

# 카드 입력
for i in range(1,N+1):
    card.append(i)

# print(card)

# 한 개 이상의 카드 남아있는 경우에만~
while len(card) != 1:
    print(card.pop(0), end=' ')
    card.append(card.pop(0))

print(card.pop())