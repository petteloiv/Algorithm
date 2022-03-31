# 자연수 N과 M이 주어졌을 때
# 1 ~ N까지 자연수 중에서 중복 없이 M개를 고른 수열

import sys
sys.stdin=open('input.txt')

def Sooyeol():
    global result

    # 숫자 채워지면 프린트
    if len(result) == M:
        a = ' '.join(map(str,result))
        print(a)

    # 숫자 하나씩밖에 없으니까 있는지 없는지 확인만해도 처리 가능하다
    for r in range(1,N+1):
        if r not in result:
            result.append(r)
            Sooyeol()
            result.pop()


N, M = map(int, input().split())
# print(N, M)

result = []

Sooyeol()