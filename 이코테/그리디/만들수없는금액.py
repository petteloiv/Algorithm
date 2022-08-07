# N개의 동전 이용해 만들 수 없는 양의 정수 금액 중 최솟값
# 그냥 1부터 쭉 돌리면서 화폐단위로 만들 수 있는지 없는지 확인하면
# 느릴까?

# 앞에서부터 확인
# 누적된 동전 금액만큼은 만들 수 있다 ...


n = int(input())
coin = list(map(int, input().split()))
coin.sort()

ans = 1

for i in coin:
    if ans >= i:
        ans += i
    else:
        break

print(ans)