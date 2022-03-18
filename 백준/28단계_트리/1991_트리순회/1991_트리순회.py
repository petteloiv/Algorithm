


import sys
sys.stdin=open('input.txt')

# 전위순회
# 가장 먼저 node 값이 . 인가 확인 -> . 이면 탐색 X 그냥 리턴
def preorder(node):
    if node == '.':
        return
    pre.append(node)
    preorder(tree[node][0])
    preorder(tree[node][1])


# 중위순회
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    in_order.append(node)
    inorder(tree[node][1])

# 후위순회
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    post.append(node)


N = int(input())

# 처음에 리스트로 받아왔는데 아스키 사용 안하면 힘들거같아서
# 딕셔너리로 변경

tree = {}

for i in range(N):
    node, lc, rc = map(str, input().split())
		# node : 부모노드 / 부모노드를 키로 해서 밸류에 왼쪽, 오른쪽 자식 넣기
    tree[node] = [lc, rc]

# 순서 저장할 리스트
pre = []
in_order = []
post = []

preorder('A')
inorder('A')
postorder('A')

# 리스트 문자열로 변환해서 출력
pre = ''.join(map(str,pre))
in_order = ''.join(map(str,in_order))
post = ''.join(map(str,post))

print(pre)
print(in_order)
print(post)