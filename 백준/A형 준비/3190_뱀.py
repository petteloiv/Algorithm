# 문제 정의
#  사과를 먹으면 뱀 길이 늘어남
# 벽 / 자기 자신의 몸과 부딪히면 게임 끝

# 방향 설정하는게 좀 어렵다
# 처음에는 오른쪽

# 보드 크기
N = int(input())
# 사과의 개수
K = int(input())
# 사과의 위치
apple = list(map(list,input().split()) for _ in range(K))
# 방향 변환 횟수
L = int(input())
# 방향 변환 정보
direction = list(map(list,input().split()) for _ in range(L))
