
# 테스트 케이스 수 
T = int(input())

for i in range(1,T+1):
    num = list(map(int, input().split()))
    a = num[0]
    b = num[1]
    print(a+b)