
import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    # n개 화물의 무게
    W = list(map(int, input().split()))
    # m개 트럭의 적재용량
    T = list(map(int, input().split()))

    # 옮겨질 화물 무게 계산
    cnt = 0

    # 오름차순 정렬시키기 ..
    W.sort()
    T.sort()

    # 트럭 개수만큼 순회,,
    for i in range(len(T)-1, -1, -1):
        # 무게 가장 무거운 것부터 돌면서 트럭으로 옮길 수 있는지 확인
        # 옮길 수 있다면 cnt에 더하고 리스트에서 삭제 (옮겼으니까 ,,)
        # 1트럭 1컨테이너니까 옮긴 즉시 break 하고 다음 트럭 확인
        for j in range(len(W)-1,-1,-1):
            if T[i] >= W[j]:
                cnt += W[j]
                W.remove(W[j])
                break

    print(f'#{tc} {cnt}')