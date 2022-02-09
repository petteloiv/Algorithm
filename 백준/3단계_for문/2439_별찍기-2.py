#첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

# trial 1 -  런타임에러
# n = int(input())

# for i in range(1, n+1):
#     print(''*n-i,'*'*i)


# trial 2 - 출력 형식이 잘못 되었습니다.
n = int(input())

for i in range(1, n+1):
    print(' '*(n-i),'*'*i)

# 내 코드랑 뭐가 다르지 ..? 
# 알아냈다.. , 가 아니라 + 였다..
# 문자열끼리 더하는거였음 ..
a=int(input())
for i in range(1,a+1):
    print(" "*(a-i) + "*"*i)