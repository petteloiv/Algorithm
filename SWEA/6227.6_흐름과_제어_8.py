# 100~300 사이의 숫자
# 각각의 자리 숫자가 짝수인 숫자를 찾아
# , 로 구분해 출력 

# trial 1 
# 답은 맞게 나오는데 왜인지 통과가 안된다 .. 
# 이유를 찾았다.. 십의자리수 홀수 거르기가 안됨 ㅠ 

for i in range(100,301):
    # 일단 2로 나눠서 1의 자리 짝수 확인 
    if (i % 10) % 2 == 0 :
        if i > 287:
            print(i)
            break
        if ((i % 100) // 10) % 2 == 0 and (i // 100) % 2 == 0:
            print(i, end=',')


# answer key
# 1의 자리 %10 나머지 
# 10의 자리 %100 나머지 //10
# 100의 자리 //100