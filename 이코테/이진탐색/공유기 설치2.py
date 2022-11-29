import sys

N, C = map(int,sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(N)]
house.sort()

# 가장 작은 간격 : 1
# 가장 넓은 간격 : 끝에서 끝 ..
# 시작점, 끝점으로 잡는당
start = 1
end = house[-1] - house[0]
distance = 0

def check_distance(start, end):
    if start > end:
        return

    mid = (start + end) // 2
    wifi = 1
    now_index = 0

    for i in range(N):
        if house[i] >= house[now_index] + mid:
            wifi += 1
            now_index = i

    if wifi >= C:
        global distance
        distance = max(distance, mid)
        check_distance(mid+1, end)
    else:
        check_distance(start, mid -1)

check_distance(start, end // (C-1)+1)
print(distance)