# 팩토리얼 구하기..
# 팩토리얼 = 1 ~ N까지 모든 곱 

N = int(input())

def Factorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * Factorial(n-1)

print(Factorial(N))