
# 기존 A+B 코드 사용했더니
# 시간초과 남... 

# T = int(input())

# for i in range(1,T+1):
#     num = list(map(int, input().split()))
#     a = num[0]
#     b = num[1]
#     print(a+b)

'''
# 문제에서 제시한 sys.stdin.readline 사용해보기 
# 반복문으로 여러줄 입력받는 상황 = 반드시 사용할 것 ..

# 한 개의 정수 입력받을 때 
# 한 줄 단위로 입력 받기 때문에 \n 가 끝에 끼어있다.. 
import sys
a = int(sys.stdin.readline())

# 정해진 개수 정수 한 줄에 입력받을 때 
import sys
a,b,c = map(int,sys.stdin.readline().split())

# 임의 개수 정수 한줄 입력 -> 리스트 저장
import sys
data = list(map(int,sys.stdin.readline().split()))

# 임의 개수 정수 n줄 입력.. 2차원 리스트에 저장 
import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

'''


import sys 

T = int(input())
for i in range(1,T+1):
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)