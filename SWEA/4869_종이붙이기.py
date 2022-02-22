# 세로는 항상 20으로 고정 / 가로크기만 변화
# N = 10의 배수. 항상 맞아떨어질 것
# stack과 memoization 사용해보기
# 최대한 DP 활용해서 풀어보기....


# stack..

import sys
sys.stdin=open("input.txt")

def Paper_memo(N):
    # global 에 있는 memo 참고 ,,
    global memo
    # N > 2 이고 (1,2 값은 넣어둠) 메모 길이가 N+1 보다 작을때
    # N이 아닌 이유는 ,, memo에 0값도 넣어뒀기 때문..?
    if N > 2 and len(memo)<=N:
            # 찾은 규칙 따라 값을 memo에서 찾고 추가해주기
            memo.append((Paper_memo(N-1) + Paper_memo(N-2)* 2))
    # N번째 값 리턴
    return memo[N]

# 메모 .. 0 (인덱스 맞추기용)
# N이 10, 20일 경우 케이스 넣어둠
memo = [0,1,3]


T = int(input())

for tc in range(1,T+1):
    # 입력 받은 N 10의 배수니까 //10 해준다
    # 그냥 인덱스 맞추기 편할거같아서 ..
    N = int(input()) // 10
    # 출력
    print(f'#{tc} {Paper_memo(N)}')