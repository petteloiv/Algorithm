# 소수 :  1과 자기 자신밖에 약수가 없는 수
# 0,1 을 아예 배제하고 range를 잡는다. 
# 자기 자신으로 나눠지는 걸 피하기 위해 n을 포함시키지않는다.
# 2~n-1 범위 중 나머지가 없게 나눠지면.. 소수가 아니다. 

n = int(input())

def function(n):
    for i in range(2, n):
        if n % i == 0:
            print('소수가 아닙니다.')
            return
    else:
        print('소수입니다.')
        return
    
print(function(n))