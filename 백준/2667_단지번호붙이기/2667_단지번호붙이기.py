
import sys
sys.stdin=open('input.txt')

N = int(input())

arr = [list(map(int, input())) for _ in range(N)]

# print(arr)

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

count = 0
result = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            count += 1
            ans = 1
            q = []
            q.append([i,j])
            arr[i][j] = 0

            while q:
                si, sj = q.pop(0)
                for d in range(4):
                    ni = si + di[d]
                    nj = sj + dj[d]

                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1:
                        ans += 1
                        arr[ni][nj] = 0
                        q.append([ni,nj])
            result.append(ans)

result.sort()

print(count)
for i in range(len(result)):
    print(result[i])

