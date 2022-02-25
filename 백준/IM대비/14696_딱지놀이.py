import sys
sys.stdin=open("input.txt")

# 4개수 세는 함수
# 4 개수가 같으면 3 세는 함수 호출
def Countfour(a,b):
    if a.count(4) > b.count(4):
        return ans.append('A')
    elif a.count(4) < b.count(4):
        return ans.append('B')
    else:
        return Countthree(a,b)

# 3 세는 함수
# 3 개수 같으면 2 세는 함수 호출
def Countthree(a,b):
    if a.count(3) > b.count(3):
        return ans.append('A')
    elif a.count(3) < b.count(3):
        return ans.append('B')
    else:
        return Counttwo(a,b)

# 2 세는 함수
# 2 개수 같으면 1 세는 함수 호출
def Counttwo(a,b):
    if a.count(2) > b.count(2):
        return ans.append('A')
    elif a.count(2) < b.count(2):
        return ans.append('B')
    else:
        return Countone(a,b)

# 1 세는 함수
# 개수 같으면 'D' 입력
def Countone(a, b):
    if a.count(1) > b.count(1):
        return ans.append('A')
    elif a.count(1) < b.count(1):
        return ans.append('B')
    else:
        return ans.append('D')


# 승부 결과 저장할 리스트
ans = []
N = int(input())
for i in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 전체리스트에서 숫자 개수 뽑아내기
    # 숫자 개수가 도대체 무슨 의미가 있는지 모르겠다 ..
    an = a.pop(0)
    bn = b.pop(0)

    # 보충교수님이 IM에서는 내장함수 쓰라길래
    # 기쁘게 내장함수 사용 ..
    a.sort()
    b.sort()

    # 만들어둔 함수 사용
    Countfour(a, b)

# 저장된 결과 리스트에서 하나씩
# 뽑아서 출력
for i in range(len(ans)):
    print(ans[i])

