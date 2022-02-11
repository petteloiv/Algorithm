# 9개의 서로 다른 자연수
# 최댓값을 찾고, 몇번째 수인지 구하는 프로그램 

# 자연수 < 100
# 출력 : 최댓값 \n 몇번째 수 

numbers = []
for i in range(9):
    numbers.append(int(input()))

# print(numbers)

# 위치, 최댓값 저장할 변수
idx = 0 
maxnumber = 0 

for i in range(len(numbers)):
    if numbers[i] > maxnumber:
        idx = i
        maxnumber = numbers[i]
print(maxnumber)
# 인덱스 0부터 셌는데 숫자는 1부터 세니까 인덱스 +1 
print(idx+1)