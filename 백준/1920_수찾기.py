# N개의 정수 a[1], a[2], a[3], .... a[n]이 주어져 있을 때,
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성

# input
# 자연수 N
# N개의 정수 ...
# M
# M개의 수 -> 얘가 A안에 존재하는지 알아내면 된다!

# output
# M개의 줄에 답 출력
# 존재 - 1, 존재하지않으면 - 0

# 1. 시간 초과

# n = int(input())
# numbers = list(map(int, input().split()))
#
# m = int(input())
# check = list(map(int, input().split()))
#
# for c in check:
#     if c in numbers:
#         print('1')
#     else:
#         print('0')


n = int(input())
numbers = set(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

for c in check:
    if c in numbers:
        print(1)
    else:
        print(0)
    # print(1) if c in numbers else print(0)