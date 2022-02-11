# ------------문제 정의 --------------#

# X의 각 자리가 등차수열 이루면 == 한수 

# N으로 범위 받고 
# 개수 출력 변수 
# 각 수의 차이 .. 입력해서 비교할 변수 

# -------- 알고리즘 풀이 -------# 


def Hansu(n): 
    # 입력한 숫자 ~ 범위 지정해 사용할 것 .. 
    n = int(n)
    # 리턴할 값 (한수 개수 더할 변수)
    cnt = 0
    # 1부터 입력 받은 숫자까지 순회
    for i in range(1,n+1):
        # 숫자.. 나눠서 리스트로 변환
        number = list(map(int, (' '.join(str(i))).split()))
        # 리스트 길이가 3보다 작으면 한수 += 1 
        # 1 ~ 99 까지는 전부 차이가 하나 나기 때문에 한수.. 
        if len(number) < 3 :
            cnt += 1
        else:
            # 기본 차이값 지정 
            basic = number[1] - number[0]
            # 전체 리스트에서 i+1 - i 값이 기본 차이값과 같은지 파악 (1,000보다 작은 수이므로 무조건 세자리)
            for i in range(1, len(number)-1):
                # 차이값과 같으면 한수 
                if number[i+1] - number[i] == basic:
                    cnt += 1 
                # 다르면 한수가 아니다 .. 
                else:
                    cnt += 0
    return cnt 

print(Hansu(input()))
