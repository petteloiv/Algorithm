import sys
sys.stdin=open('input.txt')

# --------- 테케 10개 중 6개 -----------#
# 카드 뽑아가는 중간에 이길 수 있다 ,,,는 걸 생각을 못하고 만들었다..

# -----------------다시 만듦...---------------#

# triplet 확인 함수
def Triplet(r):
    for i in range(len(r)):
        if r.count(r[i]) >= 3:
            return 1
    return 0

# run 확인 함수
def Run(r):
    for i in range(len(r)):
        # r[i] 기준 .. 해당값 연속된 값이 있으면 run (3개만 찾으면 된다,,,)
        if r[i]+1 in r and r[i]+2 in r:
            return 1
    return 0

T = int(input())

for tc in range(1,T+1):
    lst = list(map(int, input().split()))
    # print(lst)

    # 플레이어1,2가 뽑아간 카드 저장할 리스트
    p1 = []
    p2 = []

    # 플레이어 1, 2 카드 번갈아 가져가기
    for i in range(0,12,2):
        p1.append(lst[i])
        p2.append(lst[i+1])

        # 카드 3장 이상 받았을 때부터 검사 시작,,,
        if i >=3:
            # 왜 1번부터 검사하냐면 얘가 카드를 먼저 받으니까 ..
            if Triplet(p1) == 1 or Run(p1) == 1:
                print(f'#{tc} 1')
                break
            elif Triplet(p2) == 1 or Run(p2) == 1:
                print(f'#{tc} 2')
                break

    # 끝까지 이긴 사람이 없다면 무승부
    else:
        print(f'#{tc} 0')

