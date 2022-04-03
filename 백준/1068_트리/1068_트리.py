import sys
sys.stdin=open('input.txt')


# 트리를 삭제하면서 생기는 루트 노드 있다! 이 부분 처리해주기 ...
# 처리해야하는데 너무 졸려서 ,,, 처리를 못하겠다 ,,,


N = int(input())
lst = list(map(int, input().split()))
delete = int(input())
# print(lst)
tree = [[] for _ in range(N)]
# print(tree)
leaf = []

# tree 리스트에 자식 노드 모아서 입력하기
for i in range(N):
    if lst[i] == -1:
        continue
    else:
        tree[lst[i]].append(i)

# print(tree)
erased = []
q = []

erased.append(delete)
q.append(delete)

while q:
    d = q.pop()
    for i in range(len(tree[d])):
        erased.append(tree[d][i])
        q.append(tree[d][i])

# 원래 리프 노드 번호 리스트로 만들기
for i in range(N):
    if i not in lst:
        leaf.append(i)

cnt = 0
for i in range(len(leaf)):
    if leaf[i] not in erased:
        cnt += 1

print(cnt)