# 아홉개의 자연수 주어진다 ..
# 부분집합 수가 7인 것 찾아서
# 그 중에 합이 100 되는 것 찾기
# 그 다음에 오름차순으로 출력

import sys
sys.stdin=open("input.txt")

def Bubble(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i -1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


dwarf = [(int(input())) for _ in range(9)]
N = len(dwarf)

part = []

for i in range(1<<N):
    ppart = []
    for j in range(N):
        if i&(1<<j):
            ppart.append(dwarf[j])
    part.append(ppart)

seven = []
for i in part:
    if len(i) == 7:
        seven.append(i)

# print(seven)


for i in seven:
    if sum(i) == 100:
        # print(i)
        b = Bubble(i)
        # print(b)
        for j in range(len(b)):
            print(i[j])
        break


