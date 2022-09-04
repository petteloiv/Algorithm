# 죠르디의 인생 2막 : 주택 건축 사업
# 기둥 & 보 이용해 벽면 구조물을 자동으로 세우는 로봇 동작 시뮬레이션 프로그램
# 프로그램 설명
# 2차원 가상 벽면에 기둥과 보 이용한 구조물 설치 가능
# 기둥 & 보 => 길이가 1인 선분
# 기둥 : 바닥 위, 보의 한쪽 끝 부분 위, 다른 기둥 위
# 보 : 한쪽 끝부분이 기둥 위, 양쪽 끝부분이 다른 보와 동시 연결
# 바닥 : 벽면의 맨 아래 지면
# 격자선의 교차점에 걸치지 x / 격자 칸의 각 변에 정확히 일치하게 설치 가능
# 기둥 & 보 삭제 기능 O : 삭제 후에도 조건 만족 필수

# input
# n 5 <= n <= 100
# build_frame : 세로 1<= <= 1,000 가로 4
# [x, y, a, b] 형태
# x,y : 설치 또는 삭제할 교차점의 좌표 [가로, 세로]
# a : 설치 또는 삭제할 구조물 종류 0 = 기둥, 1 = 보
# b : 구조물 설치 혹은 삭제 여부 0 = 삭제, 1 = 설치
# 벽면 벗어나게 설치 X 바닥에 보 설치 X
# 교차점 좌표 기준으로 보는 오른쪽 기둥은 위쪽으로 설치/삭제

# output
# 가로 길이가 3인 2차원 배열 (좌표 담기 필수)
# [x,y,a] 형식
# x 좌표 기준으로 오름차순 정렬 / 같으면 y 좌표 기준으로 오름차순
# 둘다 같은 경우 기둥 - 보

# 추가, 제거하고 조건 충족 확인 -> 충족 O : pass / 충족 X : 다시 추가 or 제거
# 조건 충족하는 함수 만들기

def solution(n, build_frame):
    ans = set()
    for x,y,a,b in build_frame:

        # 삭제!
        if b == 0:
            ans.remove((x,y,a))
            # 조건 충족 못했으면 다시 더해주기
            if not Check(ans):
                ans.add((x,y,a))
        # 추가!
        else:
            ans.add((x,y,a))
            # 조건 충족 못했으면 다시 빼주기
            if not Check(ans):
                ans.remove((x,y,a))

    # 리스트형으로 변화시키기
    ans = list(map(list,ans))
    ans.sort(key=lambda x: (x[0], x[1], x[2]))
    return ans

    # 정렬하기

def Check(ans):
    # 0 = 기둥, 1 = 보
    for x,y,a in ans:
        # 기둥일 때
        if a == 0:
            if (x,y-1,0) in ans or (x-1,y,1) in ans or (x,y,1) in ans or y == 0:
                continue
            else:
                return False
        # 보일 때
        if a == 1:
            if (x,y-1,0) in ans or (x+1, y-1, 0) in ans or ((x-1,y,1) in ans and (x+1,y,1) in ans):
                continue
            else:
                return False
    return True