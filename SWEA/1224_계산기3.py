import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    basic = list(input())
    # print(basic)
    cal = '()+*'

    # 1. 중위계산식 변환
    num = []
    stack = []

    for i in basic:
        # 연산자일 경우 ...
        # 1. 여는 괄호 무조건 추가 가능
        if i == '(':
            stack.append(i)
            continue
        # 2. 덧셈 .. 스택 비거나 스택의 탑이 ( 일때 추가
        elif i == '+':
            while len(stack) > 0:
                if stack[-1] == '(':
                    break
                else:
                    num.append(stack.pop())
            stack.append(i)
            continue
        # 3. 곱셈 ... 스택 탑이 * 아니기만 하면 된다
        elif i == '*':
            while stack[-1] == '*':
                num.append(stack.pop())
            stack.append(i)
            continue
        # 4. 닫는 괄호
        # 여는 괄호 나올때까지 다 pop
        # 마지막에 여는 괄호 빼서 버려주기
        elif i == ')':
            while stack[-1] != '(':
                num.append(stack.pop())
            stack.pop()
        # 5. 피연산자 .. 그냥 더해준다
        else:
            num.append(i)


    # 마지막으로 스택에 남아있는 것들처리
    while len(stack) > 0:
        num.append(stack.pop())

    # 계산 ..
    calcul = []

    for i in num:
        # 피연산자는 스택에 추가
        if i != '+' and i != '*':
            calcul.append(i)
        else:
            n1 = int(calcul.pop())
            n2 = int(calcul.pop())
            # 더하기 연산자
            if i == '+':
                calcul.append(n1 + n2)
            # 곱하기
            else:
                calcul.append(n1 * n2)

    # 다 계산한 다음 calcul의 top을 프린트
    print(f'#{tc} {calcul.pop()}')