# 숫자에 대해 제곱 구하는 함수 정의 
# 숫자를 콤마로 구분해 입력하면 
# 정의한 함수 이용해 제곱 값 출력 

# input 2,3
# output 
# square(2) => 4
# square(3) => 9


# trial 1 
# 답은 제대로 나오는데 
# 오답 

# def double(x, y):
#     double1 = x ** 2
#     double2 = y ** 2
#     answer = f'square({x}) => {double1}' + '\n' + f'square({y}) => {double2}'
#     return answer 

# print(double(2, 3))

# trial 2 
# 제곱을 구하는 함수 정의 .... 

a = input()
def double():
    # 문자열에서 빼와서 숫자로 변환 .. .
    result = ''
    cal = 0 
    for i in range(len(a)+1):
        cal += a[i] ** 2 
        result += f'square({a[i]}) => {cal}'
    return result

print(double(input())) 
        


# a = input()
# print(a[0], int(a[0]))