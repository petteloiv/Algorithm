import sys
sys.stdin=open("sample.txt")

# 런타임에러난다
# 분명 어디선가 ... 조건을 빼먹은거같은데

#남학생일때
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
    for i in range(1, N//2):
        # 역시 이 조건을 빠트렸다 ...
        # 비교할 양쪽이 없는 경우 / 또는 길이가 2 이하라서 양쪽이 없는 경우 ..
        try:
            if n ==1 or n == N or len(switch) <3:
                break
            else:
                if switch[n - i] == switch[n + i]:
                    change.append(n-i)
                    change.append(n+i)
                else:
                    break
        except:
            continue
    for i in change:
        if switch[i] == 1:
            switch[i] = 0
        else:
            switch[i] = 1

T = int(input())

for tc in range(1,T+1):
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

    # 출력 스타일 맞추기 .. 한 줄 20개
    # if len(switch) > 20:
    #


    # switch = ' '.join(map(str, switch))

    # if len(switch) > 20:
    #     for i in range(len(switch)):
    #         if i % 20 == 0:
    #             print(switch[i], end='\n')
    #         else:
    #             print(switch[i], end=' ')
    # else:
    #     switch = ' '.join(map(str, switch))
    #     print(switch)

    for i in range(0, N, 20):
        print(*switch[i:i+20])
