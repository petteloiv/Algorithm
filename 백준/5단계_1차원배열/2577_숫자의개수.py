# -------------문제 -------------------# 
# 세 자연수 a, b, c 준다 ..
# a * b * c 계산한 결과에
# 0~9까지 각각 숫자 몇 번씩 쓰였는지 ! 

# 카운팅 정렬 .. 반만 쓰면 될거같다 

# ----------- 풀이 ---------- #

a = int(input())
b = int(input())
c = int(input())

number = a*b*c 
numbers = list(map(int, str(number)))
# print(numbers)
counters = [0]*10 

for i in range(len(numbers)):
    counters[numbers[i]] += 1

for j in counters:
    print(j)