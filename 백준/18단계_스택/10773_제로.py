# 항상 정신없는 재현이는 돈을 실수로 잘못 부르는 사고
# 잘못된 수 부를때마다 0 외침
# 0 외칠때마다 재민이가 쓴 수 지운다

K = int(input())
stack = []

for i in range(K):
    num = int(input())
    if num != 0 :
        stack.append(num)
    else: 
        stack.pop()

print(sum(stack))
