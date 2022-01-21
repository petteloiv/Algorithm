# 어떤 양의 정수 입력
# 그 숫자에 0~9가 몇 번 사용되었는지 표시

# # 

# num = int(input())
# count = 0 

# for i in len(num):
    
# while문 사용하여 일의 자리 숫자 카운트하여 리스트에 넣기
# 마지막에 문자열로 변환 .. .

num = int(input())
count_list = [0]*10

while num>=0:
    count_list[num%10] += 1
    num = num//10

print(' '.join(map(str, [i for i in range(10)]))) 
print(' '.join(map(str, count_list)))

# 코드 참고 

num = input()
units = [0]*10

for idx in num:
    for i in range(10):
        if int(idx) == i:
            units[i] += 1

print(*range(10))
print(*units)



# output 
# 0 1 2 3 4 5 6 7 8 9
# 0 2 0 0 0 0 0 0 0 0