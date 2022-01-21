# 피보나치 수열의 결과 생성 
# 앞의 두 수의 합 == 다음 수
# 함수 안에 정수형 변수 선언
# list 만들어 일정한 숫자만큼 반복
# 아직도 잘 모르겠다 ... 

num = int(input())

def fibonaci(num):
    numbers = [1, 1]
    a = 1
    b = 1
    c = 0
    for i in range(num-2):
        c = a+b
        numbers.append(c)
        a = b
        b = c
    return numbers

print(fibonaci(10))