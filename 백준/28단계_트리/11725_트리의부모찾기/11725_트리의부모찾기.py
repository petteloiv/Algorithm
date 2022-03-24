# 루트 없는 트리 주어짐
# 트리의 루트 1
# 각 노드의 부모

# 첫째줄 : 노드의 개수 N
# N-1개 줄에 트리 상에서 연결된 두 정점
# 각 노드의 부모 노드 번호 2번부터 순서대로 출력

import sys
sys.stdin=open('inpput.txt')

T = int(input())

for tc in range(1,T+1):
    # 노드의 개수
    N = int(input())
    # N-1 개의 줄에 출력
    arr = list(list(map(int, input().split())) for _ in range(N-1))
    print(arr)

    # 앞이 부모,.. 뒤가 자식
    # 자식 인덱스에 부모 값 넣어서 출력하면 되지 않을까 ...

    v = [0] * (N+1)

    for i in arr:
        v[i[1]] = i[0]


    print(v)

