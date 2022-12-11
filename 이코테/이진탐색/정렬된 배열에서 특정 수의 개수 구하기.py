# N개 원소 포함 수열 -> 오름차순으로 정렬되어있음
# 이 수열에서 x가 등장하는 횟수는?
# ex) {1, 1, 2, 2, 2, 2, 3} 일때 x = 2 라면
# 현재 수열에서 값이 2인 원소 = 4개 -> 4 출력~
# 시간 복잡도 고려

# input)
# N x
# N개의 원소

# output
# 하나도 없다면 -1 출력 / 나머지는 개수 출력

from collections import Counter

N, x = map(int,input().split())
numbers = list(map(int, input().split()))

x_counter = Counter(numbers)
print(x_counter)

if x_counter[x] == 0:
    print(-1)
else:
    print(x_counter[x])