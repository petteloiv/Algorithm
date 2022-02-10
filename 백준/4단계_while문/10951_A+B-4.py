# --------문제 정의 -----------# 
# 두 정수 A와 B 입력받고
# A+B 출력 

# 각 테스트케이스마다
# A + B 출력

# ------- 알고리즘 풀이 ----------# 

# trial 1 - 종료 조건 못 만들어서 틀림 

# a, b = map(int, input().split())

# # while 문 종료 조건 파악이 어렵다 .. 
# while a and b:
#     print(a+b)
#     a, b = map(int, input().split())

# trial 2 

# 예외처리!!!!!!!!! 왜 생각 못했ㅈㅣ
# try except 사용하기 
# try except else finally

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break