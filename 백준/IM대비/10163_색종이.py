import sys
sys.stdin=open("input.txt")

N = int(input())
# 좌표, 너비, 높이 리스트로 받아오기
paper = [list(map(int,input().split())) for _ in range(N)]

arr = [[0]*1001 for _ in range(1001)]

# print(paper)

for t in range(N):
    x, y, w, h = paper[t]
    for i in range(x, x+w):
        for j in range(y,y+h):
            # 값 추가가 아니라 덮어주면서
            arr[i][j] = t+1


total = []
for k in range(1,N+1):
    count = 0
    for i in arr:
        for j in i:
            if j == k:
                count += 1
    total.append(count)

for i in total:
    print(i)