# 피보나치수는 0과 1로 시작 
# 본인 앞 두 숫자의 합... 


N = int(input())


def Fibo(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)


print(Fibo(N)) 
