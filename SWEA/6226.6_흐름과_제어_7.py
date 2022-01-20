# 1~200 사이의 정수 중
# 1. 7의배수
# 2. 그러나 5의 배수는 아닌 
# 3. , 로 구분된 문자열 구성해 출력 
# 맨 마지막 , 는 제외해야한다.. 

for i in range(1,201):
    numbers = ''
    if i % 7 == 0 and i%5 !=0:
        if(i>195):
            print(i)
            break
        print(i, end=',')


# 맨 처음 오답 
# 196 이후의 , 를 어떻게 제거해야할 지 몰랐다 ..
# 추가해서 코드 수정 !  

for i in range(1,201):
    numbers = ''
    if i % 7 == 0:
        if i % 5:
           if i > 195:
               print(i)
               break
           else:
            numbers += str(i) 
            print(numbers, end = ',')


