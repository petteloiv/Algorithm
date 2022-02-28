# N개의 수가 주어졌을 때 이를 오름차순으로 정렬

# 수의 개수
N = int(input())

num = []
for i in range(N):
    num.append(int(input()))

# 오름차순으로 정렬
# 버블 정렬 사용

for i in range(N-1,-1,-1):
    for j in range(i):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]

for i in range(N):
    print(num[i])
