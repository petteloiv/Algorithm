# ---------문제 정의 -----------# 

# O는 문제 맞은거고,, X는 문제 틀린 것 
# 그 문제의 점수 = 연속된 O의 개수
# OOXXOXXOOO
# 1200100123 점 

# 이중 for문을 사용해야 할 것 같은 느낌이 온다.. 

# -----------알고리즘 풀이 --------------# 

# 테스트 케이스 숫자 
T = int(input())


for tc in range(T):
    # O, X 로 나눠서 리스트에 담기
    score = list((' '.join(input())).split())
    # print(score)
    
    # 최종 출력값 변수
    result = 0
    # 내 앞에 O 개수 셀 변수
    cnt = 0

    # 리스트 전체 순회
    for i in range(len(score)):
        # i 위치의 값이 O 이라면
        if score[i] == 'O':
            # 앞의 값이 O이라면
            # O개수 + 1 
            # cnt 만큼 더해준다
            if score[i-1] == score[i]:
                cnt += 1
                result += cnt
            # 아니라면,.,. (앞의 값 X)
            # 결과에 1 더해주고 O개수 카운트에도 +1 
            else:
                result += 1 
                cnt += 1
        # i위치 값이 X 라면
        # O개수 초기화
        else:
            cnt = 0
    print(result)
