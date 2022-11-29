# 고정점 : 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
# ex) a = {-15, -4, 2, 8, 13}
# a[2] = 2 -> 고정점 = 2
# 하나의 수열 / N개의 서로 다른 원소 포함. 모든 원소 오름차순!
# 고정점이 있다면 출력 (최대 1개) 없다면 -1 출력

# input)
# N
# N개의 원소

# 이미 정렬되어있는 수열 -> 바로 이진탐색 고고고
# 인덱스 <-> 값 비교
# 인덱스보다 값이 더 크다 -> 왼쪽으로 이동
# 인덱스보다 값 작다? -> 오른쪽


N = int(input())
numbers = list(map(int, input().split()))

def find_binary(numbers, start, end):
    while start <= end:
        mid = (start+end) // 2

        # 고정점 있는 경우
        # 최대 하나니까 찾으면 바로 break 걸기
        if numbers[mid] == mid:
            return mid
            break
        # 인덱스 < 값 (왼쪽)
        elif numbers[mid] > mid:
            end = mid-1
        # 인덱스 > 값 (오른쪽)
        else:
            start = mid+1
    return -1

print(find_binary(numbers, 0, N-1))