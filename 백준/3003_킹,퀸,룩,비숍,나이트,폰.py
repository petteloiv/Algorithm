chess = [1, 1, 2, 2, 2, 8]

white = list(map(int, input().split()))

for i in range(6):
    if i == 5:
        print(chess[i] - white[i])
    else:
        print(chess[i] - white[i], end=" ")