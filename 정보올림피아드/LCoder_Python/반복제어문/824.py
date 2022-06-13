# 이거 0점 처리됨 ㅠㅠㅠ
# lst = []
# while True:
#     n = int(input())
#     if n >= 100:
#         print(sum(lst))
#         print("%.1f"%(sum(lst)/len(lst)))
#     else:
#         lst.append(n)
#


sum=0
num=0
while True:
    a=int(input())
    sum+=a
    num+=1
    if a>=100:
        break
print(sum)
print("%.1f" %(sum/num))