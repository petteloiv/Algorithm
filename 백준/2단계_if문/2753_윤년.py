# 윤년 : 연도가 4의 배수이면서 100의 배수 아닐때
# 윤년 : 4의 배수 & 400의 배수일 때 
# 윤년이면 1, 아니면 0 출력 

year = int(input())

if year%4 == 0 and year%100 != 0:
    print(1)
elif year%400 ==0 :
    print(1)
else:
    print(0)