# N개의 수가 주어졌을때 오름차순으로 정렬하는 프로그램
# 카운팅정렬 사용하기 ..
# 카운팅정렬은 준비해야할게 너무 많아서 귀찮다

import sys

# input이 용량을 많이 차지한다고 한다 ..
n = int(sys.stdin.readline())
# 최대 숫자
num_list = [0] * 10001

# 인풋받은값을 인덱스로해서 1 추가
for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

# 전체 리스트 순회하면서
# 값이 0이 아니라면 (최소 1개 있다는 뜻)
for i in range(10001):
    if num_list[i] != 0:
        # 들어있는 개수만큼 반복하면서 프린트
        for j in range(num_list[i]):
            print(i)



# 기존 카운팅 정렬에서 메모리 초과 나서 구글 검색 돌림 ..
# 실패 코드
N = int(input())

number = []
sort_num = [0] * len(number)
for i in range(N):
    number.append(int(input()))

count = [0]*(len(number)+1)



for i in range(len(number)):
    count[number[i]] += 1

for j in range(1,len(count)):
    count[j] = count[j-1] + count[j]

# 이제 number의 맨 끝 값부터 순회 ..
# count[끝값] -= 1 을 sort_num 인덱스... 맨 끝 숫자 넣는다

for i in range(len(sort_num)-1, -1, -1):
    count[number[i]] -= 1
    sort_num[count[number[i]]] = number[i]

for t in sort_num:
    print(t)
