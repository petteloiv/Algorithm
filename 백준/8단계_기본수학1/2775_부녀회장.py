# ------------문제 정의 -------------# 

# 아파트 거주 조건 
# a층의 b호에 살려면 
# a-1층의 1호 ~ b호 사람 수 합 만큼 데려와야한다. 

# 비어있는 집 없음 X 
# k층 n호에는 몇 명이 살고있는지! 

# 아파트 zero층~ 
# 각 층 1호 ~ 
# zero층의 i호에는 i명이 산다 ... 

# 일단 zero층 사람 숫자 먼저 구하기 

# ---------------알고리즘 풀이 --------------# 

# T = int(input())

# for tc in range(1,T+1):
#     k = int(input())
#     n = int(input())

#     ppl = []
#     # 일단 0층 사람 먼저 구하기 
#     for i in range(1,n+1):
#         ppl.append(i)
#     # print(ppl)

#     # k층 n호실 사람 수 구하기
#     # n호실 = 기존값 + n-1호실 사람 더하기 .. 
#     for i in range(k):
#         for j in range(1,n):
#             ppl[j] += ppl[j-1]

#     print(ppl[-1])

        

T = int(input())
for tc in (1,T+1):
    k = int(input()) #k층
    n = int(input()) #n호 에는 몇명이 살고 있을까?

    person = list(range(1,n+1)) #0층에서 n호까지 사람 수 
    floor = 0 #0층에서 k층까지 반복
    while floor!=k: #층수가 k가 아닌동안 한층씩 높여가면서 반복
        for i in range(1,n+1): #1에서 n호까지
            person[i+1]+=person[i] #n-1호까지의 합이 n호에 누적됨
        floor += 1 #1층씩 증가 
    print(person[-1]) 