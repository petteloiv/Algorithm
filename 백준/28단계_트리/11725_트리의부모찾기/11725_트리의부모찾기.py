# 루트 없는 트리 주어짐
# 트리의 루트 1
# 각 노드의 부모

# 첫째줄 : 노드의 개수 N
# N-1개 줄에 트리 상에서 연결된 두 정점
# 각 노드의 부모 노드 번호 2번부터 순서대로 출력

import sys
sys.stdin=open('inpput.txt')

T = 2

for tc in range(1,T+1):
    N = int(input())
