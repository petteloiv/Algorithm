# 다음과 같이 팩토리얼을 구하는 함수를 정의
# 입력된 숫자에 대한 
# 팩토리얼 값

# 이거는 .. 재귀함수의 느낌이 온다 

# input 5 -> output 120

# hint 1~n까지의 곱 

# 1 * 2 * 3 * 4 * 5
# f(5) = f(4) * 5
# f(4) = f(3) * 4
# f(3) = f(2) * 3
# f(2) = f(1) * 2 =2
# f(1) = 1 *1 =1

# factorial(num) = factorial(num-1) * num 

def factorial(num):
    total = 1
    for i in range(1, num+1):
        total = factorial(i-1) * i 
        factorial(i-1)
    return total 

print(factorial(5))

# pass 

# 맞았는데 왜 맞았는지를 모르는 코드 ... 

# def factorial(5):
#     total = 1
#     for i in range(1, 6): # 1, 2, 3, 4, 5
#         total = factorial(i-1) * i 
#         factorial(i-1)
#     return total 

