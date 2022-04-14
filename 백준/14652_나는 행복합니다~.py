# 2차원 배열에 숫자 다 집어넣고
# 숫자 값의 인덱스 뽑아서 ... 출력

n, m, k = map(int, input().split())

arr = [[0]*n for _ in range(m)]

cnt = 0
ans = []
for i in range(n):
    for j in range(m):
        if cnt == k:
            ans.append(i)
            ans.append(j)
            break
        else:
            cnt += 1

ans = ' '.join(map(str, ans))
print(ans[:3])
