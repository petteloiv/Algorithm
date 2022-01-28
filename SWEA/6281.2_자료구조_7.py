# 리스트 내포 
# list comprehension 이용해 
# 약수 리스트 출력 

# 리스트명 = [표현식 for 변수 in 반복 가능한 대상]

# trial 1 
'''
num = int(input())
divisor_num = [num % i == 0 for i in range(1, num+1)]
print(divisor_num)
'''

# 오류났다 ! ㅎㅎ 
# list comprehension 
# 리스트명 = [표현식 for 변수 in 반복 가능한 대상 if 조건문]
# 표현식이 그대로 리스트에 담기는 형태! 

num = int(input())

divisor_num = [ i for i in range(1, num+1) if num % i ==0]
print(divisor_num)