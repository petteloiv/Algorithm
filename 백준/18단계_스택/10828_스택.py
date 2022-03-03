# 정수 저장하는 스택 구현
# 입력으로 주어지는 명령 처리하는 프로그램 

# 명령 총 5개
# 1. push X -> X를 스택에 넣는다
# 2. pop -> 위에 있는 정수 빼고 그 수 출력 / 스택 비어있으면 -1 출력 
# 3. size -> 스택에 들어있는 정수 개수 출력 
# 4. empty : 스택 비어있으면 1, 아니면 0
# 5. top : 스택 가장 위에 있는 정수 출력 / 없으면 -1 



N = int(input())
stack = []
result = []
for i in range(N):
    command = input()
    if command == 'pop':
        if len(stack) > 0:
            result.append(stack.pop())

        else:
            result.append(-1)

    elif command == 'size':
        result.append(len(stack))

    elif command == 'empty':
        if len(stack) == 0:
            result.append(1)

        else:
            result.append(0)

    elif command == 'top':
        if len(stack) > 0:
            result.append(stack[-1])

        else:
            result.append(-1)

    else:
        cmd, num = map(str, command.split())
        stack.append(int(num))

for i in result:
    print(i)
