# 기술 강력 but 게임 내에서 점수가 특정 조건 만족할 때만 사용 가능
# 특정 조건
# 현재 캐릭터의 점수 === N 자릿수 기준으로 점수 N을 반으로 나누어
# " 왼쪽 부분의 각 자릿수 합 == 오른쪽 부분 각 자릿수 합" 인 상황
# 현재 점수 N 주어지면 럭키 스트레이트 사용할 수 있는 상태인지 아닌지 알려주는 프로그램
# 사용할 수 있으면 LUCKY / 없으면 READY

number = input()
n = len(number) // 2

front = sum(list(map(int,number[0:n])))
back = sum(list(map(int,number[n:])))

if front == back:
    print("LUCKY")
else:
    print("READY")

