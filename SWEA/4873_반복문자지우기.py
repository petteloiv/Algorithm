# --------------------문제 정의 ----------------------#
# 최대한 스택 사용해보기
# 지우기 -> 앞뒤 연결 -> 반복문자 생기면 다시 지우기 -> 앞뒤 연결 ...
# 맨 마지막에 남은 글자수 출력

# 스택에 넣다가 top에 중복되는게 있을 경우 pop하기.. 그 다음 ! 반복 ...


# ------------------ 알고리즘 풀이 --------------------#

import sys
sys.stdin=open("input.txt")


T = int(input())

for tc in range(1,T+1):
    words = list(map(str, input()))
    # 저장할 스택 (리스트)
    stack = []

    # 리스트 전체 순회 ..
    for i in words:
        # 스택에 아무것도 없으면 +
        if len(stack) == 0:
            stack.append(i)
        # 스택의 top값이 i와 동일하다면 -
        elif stack[-1] == i:
            stack.pop()
        # 스택 top값 != i +
        else:
            stack.append(i)

    print(f'#{tc} {len(stack)}')