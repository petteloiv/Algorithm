import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    m1 = []
    m2 = []
    m3 = []

    # 90도 회전
    # 열 우선 순회 후 뒤집어 넣기
    for j in range(N):
        ttl = []
        for i in range(N-1,-1,-1):
            ttl.append(arr[i][j])
        m1.append(ttl)

    # 180도 회전
    for i in range(N-1,-1,-1):
        ttl = []
        for j in range(N-1,-1,-1):
            ttl.append(arr[i][j])
        m2.append(ttl)

    #270도 회전
    for j in range(N-1,-1,-1):
        ttl = []
        for i in range(N):
            ttl.append(arr[i][j])
        m3.append(ttl)

    total = list(map(list,zip(m1,m2,m3)))

    print(f'#{tc}')
    for i in range(len(total)):
        printt = []
        for j in range(len(total[i])):
            printt.append(''.join(map(str, total[i][j])))
        print(' '.join(map(str, printt)))