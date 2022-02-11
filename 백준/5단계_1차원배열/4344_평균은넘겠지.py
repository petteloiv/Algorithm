# --------문제 정의 ----------# 
# 대학생 새내기의 90%는 자신이 반에서 평균은 넘는다고 생각
# ㅋㅋ...

# 입력값:
# 테스트 케이스의 개수 C / 첫 수 = 학생수 , N명의 점수
# 0 <= 점슈 <= 100 

# 평균 넘는 학생들의 비율을 반올림하여 
# 소수점 셋째 자리까지 출력 
# round.. 써야할듯하다 

# --------알고리즘 풀이 -----------# 

# 테스트 케이스 개수 
C = int(input())

for tc in range(C):

    scores = list(map(int, input().split()))
    student = scores[0]

    total = 0
    over_score = 0

    # 평균 구하기 
    for i in range(1,len(scores)):
        total += scores[i]  

    score_m = total/student  

    # 평균 넘는 학생 수 구하기 
    for i in range(1, len(scores)):
        if scores[i] > score_m:
            over_score += 1 

    # 학생들의 비율 프린트하기
    # 여기서 ValueError 났었다...
    # % 프린트 하고싶으면 %% 두개 쓰기 잊지말자..
    print('%.3f%%' % (over_score/student*100))