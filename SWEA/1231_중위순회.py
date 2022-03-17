# inorder 형식으로 순회해서 단어 읽기
# 완전 이진 트리 형식 (비어있는 노드 없음)
# 노드당 하나의 알파벳만 저장 가능
# 노드가 주어지는 순서는 그대로 ....

import sys
sys.stdin=open("input.txt")
# 1. 일단 입력 받은 값 트리에 저장
T = 10

# 완전 이진 트리 형식 & 주어진 숫자대로 ..
def in_order(v):
    if v <= N:
        in_order(v * 2)
        print(arr[v], end='')
        in_order(v * 2 + 1)

for tc in range(1, T+1):
    # 정점의 개수
    N = int(input())
    arr = [0] * (N+1)
    # input 받기
    for i in range(N):
        data = input().split()
        # 노드번호
        v = int(data[0])
        # 알파벳
        alpha = data[1]
        # 노드 번호에 알파벳 넣어주기
        arr[v] = alpha

    print(f'#{tc}', end=' ')
    in_order(1)
    print()