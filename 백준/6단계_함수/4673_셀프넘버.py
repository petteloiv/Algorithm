# ---------문제 정의 ----------# 
# 양의 정수 n에 대해
# d(n) = n + n의 일의 자리 + n의 십의 자리 ... 

# n, d(n), d(d(n)) ... 같은 무한 수열 만들 수 있다 
# n = d(n) 의 생성자 .,.. 

# 생성자가 없는 숫자 = 셀프 넘버 
# 100 보다 작은 셀프 넘버 총 13개 

# 10000보다 작거나 같은 셀프넘버를 한 줄에 하나씩 출력하는 프로그램 

#--------------알고리즘 풀이 ------------#
def Notself(n):
    result = 0
    result += n
    while n != 0:
        result += n%10
        n = n//10
    return result

# 연속된 숫자 리스트 만들기
all = list(range(1,10001))

# 생성자 두개 있는 경우 인덱스 에러난다 
# 오류 처리 필요!!!
# 생성자 있는 값들 삭제... 
for i in range(1,10000):
    try:
        all.remove(Notself(i))
    except:
        continue

for j in all:
    print(j)


