import sys
sys.stdin=open('input.txt')

N = int(input())
num = [int(input()) for _ in range(N)]
num.sort()

# 산술평균
a = sum(num) // N
# 중앙값
b = num[N//2]

# 최빈값 (여러개 있을때는 최빈값 중 두번째로 작은값 출력)
howmany = 1
c = 'notyet'

# 범위
d = max(num) - min(num)

print(a)
print(b)
print(c)
print(d)