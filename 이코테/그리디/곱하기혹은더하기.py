# 왼 -> 오 모든 숫자 확인하며 x, + 연산자 넣어 가장 큰 수 만들기
# 모든 연산 순서대로
# 0이 있을 때 제외하고 전부 x 넣으면 된다 ..

numbers = list(map(int, input()))

total = numbers[0]
for i in range(1,len(numbers)):
    if total == 0:
        total += numbers[i]
    else:
        total *= numbers[i]

print(total)