def Boys(switch, n):
    for i in range(1,N+1):
        # 자기가 받은 수의 배수일 때 상태 변화
        if i % n == 0:
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1
        else:
            continue

# 여학생일때
def Girls(switch, n):
    change = []
    change.append(n)
    for i in range(1, N):
       # 이 부분 수정함 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			 # 실행할 수 있는 코드를 먼저 넣고 나머지 다 else 처리 하자!!!!!!
        if 0<n-i and n+i<=N and switch[n - i] == switch[n + i]:
            change.append(n - i)
            change.append(n + i)
        else:
            break
    for i in change:
        if switch[i] == 1:
            switch[i] = 0
        else:
            switch[i] = 1


N = int(input())
switch = list(map(int, input().split()))
S = int(input())
lst = [list(map(int, input().split())) for _ in range(S)]

switch.insert(0, 0)

# print(lst)
for i in lst:
    # 남학생일 경우
    if i[0] == 1:
        Boys(switch, i[1])
    # 여학생일 경우
    elif i[0] == 2:
        Girls(switch, i[1])
# 인덱스 맞추기 위해서 switch 앞에 0 하나 끼워둔거 제거
switch.pop(0)

for i in range(0, N, 20):
    print(*switch[i:i+20])