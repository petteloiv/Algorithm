
import sys
sys.stdin=open('input.txt')

# 시계방향
def Clockwise(lst):
    p = lst.pop()
    lst.insert(0, p)

# 반시계방향
def Anticlockwise(lst):
    p = lst.pop(0)
    lst.append(p)

# 양 옆 톱니바퀴 회전시켜야하는지 확인하기
def check_left(now, left):
    # 값 다르다면 반대로 돌려주고
    if left < 0:
        return
    # 다시 재귀 .. 왼쪽에 남은게 없을 때까지
    if top_ni[now][6] != top_ni[left][2]:
        check_left(left, left-1)
        # 원래 톱니랑 반대 방향으로 돌리기 ..

def check_right(now, right):
    if right > 3:
        return
    if top_ni[now][2] != top_ni[right][6]:
        right(right, right+1)

# 테케 돌려보려고 이 부분 임의로 추가했습니다.
T = int(input())

for tc in range(1,T+1):
    # 톱니바퀴 입력 받아오기
    top_ni = [list(map(int, input())) for _ in range(4)]
    # print(top_ni)
    # 회전 횟수, 방향
    K = int(input())
    round_n = [list(map(int, input().split())) for _ in range(K)]


    # 회전 전의 톱니바퀴를 기준으로 돌아가는지 안돌아가는지 파악
    # 톱니들 ,, 인덱스 어떻게 처리해야 left, right 확인 함수에
    # 넣어서 쓸 수 있을까 고민
    # 회전 입력할 리스트가 따로 필요할 것 같다..

    # 점수 계산
    ans = 0
    for i in top_ni:
        if i == 0 and i[0] == 1:
            ans += 1
        elif i == 1 and i[0] == 1:
            ans += 2
        elif i == 2 and i[0] == 1:
            ans += 4
        elif i == 3 and i[0] == 1:
            ans += 8

    print(ans)


