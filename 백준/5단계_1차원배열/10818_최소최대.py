# ---------문제 ----------# 

# 첫째줄: 정수의 개수 N 
# 둘째줄: N개의 정수 

# 정수 n의 최솟값과 최댓값 공백으로 구분해 출력 

# ---------- 풀이 ---------# 

# 1. 내장함수 사용 

# n = int(input())
# numbers = list(map(int, input().split()))

# print(f'{min(numbers)} {max(numbers)}')

# 2. 내장함수 사용 X 
# 왜 틀린지 모르겠는데 틀렸다 .. 왜인지도 알려주라

n = int(input())
numbers = list(map(int, input().split()))

min_num = 1000001
max_num = 0 

for i in range(len(numbers)):
    if numbers[i] < min_num:
        min_num = int(numbers[i]) 
    if numbers[i] > max_num:
        max_num = int(numbers[i]) 

print(f'{min_num} {max_num}')

# -----------숏코딩-----------# 
# input()
# a=[int(x)for x in input().split()]
# print(min(a),max(a))