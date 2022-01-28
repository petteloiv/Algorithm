# 자료구조 : 리스트, 튜플
# 정수를 입력하면 
# 약수를 리스트에 추가해 출력하는 코드 작성 

# 1. 정수 입력 
# 2. 리턴할 리스트 만들기 
# 3. 약수 찾기 ... 
# 4. 약수 리스트에 추가해 출력 

num = int(input())

def divisor(num):
    divisor_num = []
    for i in range(1,num+1):
        if num % i == 0:
            divisor_num.append(i)
    return divisor_num

print(divisor(num))