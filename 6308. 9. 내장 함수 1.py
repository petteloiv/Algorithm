#이름과 나이 변수로 저장
name = input(홍길동)
age = int(input(20))

# 100살 되는 년도 환산하는 함수 (문제 오류로 이번년도가 2019년으로 설정)
count = 2019 + (100 - age)

print("{0}(은)는 {1}년에 {2}세가 될 것입니다.".format(name, count,100))