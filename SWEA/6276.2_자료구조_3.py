# 구구단 2단부터 9단의 결과값 중에 3의 배수거나 7의 배수인 수를 제외한 값
# 리스트 객체 result안에 각 단마다 리스트 만들어 삽입하고 이를 출력하십시오.

# 결과 [[2, 4, 8, 10, 16], [], [4, 8, 16, 20, 32], [5, 10, 20, 25, 40], [], [], [8, 16, 32, 40, 64], []]


# 반환할 객체 
from msvcrt import kbhit


result = []
# 구구단 2단부터 9단 결과값 저장할 리스트 변수
gugudan = []

#  구구단 결과값 저장 (3의 배수이거나 7의 배수 제외)

for i in range(2,10):
    gugudan = []
    for j in range(1,10):
        gugu = i * j
        if gugu % 3 == 0 or gugu % 7 == 0:
            continue
        else:
            gugudan.append(gugu)
    result += [gugudan]
print(result)