# ------------문제 정의 ----------------#

# 괄호검사!
# 파이썬 코드일수도 있고 .....? 문자열이라는 말
# 중괄호냐 소괄호냐만 제대로 파악하기

# ----------------------알고리즘 풀이 ------------------#

import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1,T+1):
    lst = list(map(str,input()))
    # print(lst)

    # 괄호 저장할 스택 (리스트)
    stack = []
    # 맨 마지막 출력때문에 만들어둔 변수 ..
    # 한번 돌 때마다 +1
    cnt = 0

    for i in lst:
        cnt += 1
        # 여는 괄호 + append
        if i =='{' or i =='(':
            stack.append(i)
        # 닫는 괄호라면 ??
        elif i == '}' or i == ')':
            # 스택이 비어있지 않다면
            if len(stack) != 0:
                # 짝 맞으면 제거
                if i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                # 짝 안맞으면 프린트하고 반복문 멈추기
                else:
                    print(f'#{tc} 0')
                    break
            # 스택이 비어있다면 ! (짝 맞출수가 없으니 조건 위배)
            else:
                print(f'#{tc} 0')
                break
        # 기타... 괄호 뺀 다른 문자 나오면 그냥 건너뛰기
        else:
            continue

    # 반복문 끝까지 돌았을 때 ,,
    # 스택 비어있으면 1, 스택 차있으면 0
    if cnt == len(lst) and len(stack) == 0:
        print(f'#{tc} 1')
    elif cnt == len(lst) and len(stack) != 0:
        print(f'#{tc} 0')
