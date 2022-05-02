def func(lst):
    # 델타 ( 현재위치, 상하좌우)
    di = [0, -1, 0, 1, 0]
    dj = [0, 0, -1, 0, 1]

    # 꽃이 차지한 자리 좌표 입력해놓기
    check = []

    # 땅값..
    result = 0

    for flower in lst:
        i = flower // N
        j = flower % N

        # 범위 벗어나면 그냥 제일 큰 값 리턴해버리기
        if i == 0 or i == N - 1 or j == 0 or j == N - 1:
            return 10000

        # 델타 돌면서 주변 땅까지 처리해주기
        for d in range(5):
            check.append((i + di[d], j + dj[d]))
            result += pot[i + di[d]][j + dj[d]]

    # 씨앗은 세개 .. 하나당 5자리씩 차지하니까 15
    if len(set(check)) == 15:
        return result
    return 10000

# 화단 한 변의 길이 ..
N = int(input())
# 화단
pot = [list(map(int, input().split())) for _ in range(N)]

# 임의의 큰 값을 price로 설정
price = 10000

# 꽃씨 세개 ... 그냥 모든 경우 다 확인해서 최소값만 갱신해주기
for i in range(N ** 2 ):
    for j in range(N ** 2):
        for k in range(N ** 2):
            lst = [i, j, k]
            price = min(price, func(lst))
print(price)
