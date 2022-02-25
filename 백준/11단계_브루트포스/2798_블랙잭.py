

N, M = map(int, input().split())
cards = list(map(int, input().split()))


max_num = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = cards[i] + cards[j] + cards[k]
            if total <= M:
                if total > max_num:
                    max_num = total

print(max_num)