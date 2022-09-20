# N개의 수로 이루어진 수열
# 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자
# 수 - 연산자 - 수 로 수식 만들 수 있당 (순서 변경 XXXXX)
# 계산 : 연산자 순서 무시하고 앞에서부터
# 나눗셈 : 정수 나눗셈으로 몫만!
# dfs에 입력받은 수열 개수만큼 계ㅖㅖㅖㅖ속 반복수행


n = int(input())
numlist = list(map(int, input().split()))

# 연산자 각각 개수!
add, sub, mul, div = map(int, input().split())

max_ans = -1000000000
min_ans = 1000000000

def dfs(i, arr):
    global add, sub, mul, div, max_ans, min_ans

    if i == n:
        max_ans = max(max_ans, arr)
        min_ans = min(min_ans, arr)

    else:
        # 연산자 있을때만 ,,
        if add > 0 :
            add -= 1
            # 기존 값 (연산자) 다음 값
            dfs(i+1, arr + numlist[i])
            add += 1
        if sub > 0 :
            sub -= 1
            dfs(i+1, arr - numlist[i])
            sub += 1
        if mul > 0 :
            mul -= 1
            dfs(i+1, arr * numlist[i])
            mul += 1
        if div > 0 :
            div -= 1
            dfs(i+1, int(arr // numlist[i]))
            div += 1

# 첫번째부터 어 시작 / 1인 이유는 숫자 개수 맞추려고
dfs(1, numlist[0])

print(max_ans)
print(min_ans)