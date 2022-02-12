# ---------문제 정의 -----------# 
# n개의 숫자 공백 없이 쓰여있음 
# 모두 합해서 출력하는 프로그램 
# 숫자의 개수 / 숫자 n개 

# ----------알고리즘 풀이--------------# 

n = int(input())
numbers = list(map(int, input()))
total = 0

for i in range(n):
    total += numbers[i]

print(total)