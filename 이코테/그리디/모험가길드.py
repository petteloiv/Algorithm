# todos = [1, 2, 3, 4, 5]
#
# isCompleted = {
#     1:True,
#     4:False
# }
#
# for todo in todos:
#     if todo not in isCompleted:
#         isCompleted[todo] = False
#         print(False)
#     else:
#         print(isCompleted[todo])


# 공포도 이상! 일 때 참여해서 여행갈 수 있다
# 1. 모험가 공포도 정렬
# 2. 그룹인원 / 그룹 변수
# 3. for문 돌면서 일단 그룹 인원에 추가해주기
# 그룹인원 = 공포도 => 그룹 +1, 인원 초기화

n = int(input())
fear = list(map(int, input().split()))

fear.sort()

member = 0
group = 0

for i in fear:
    member += 1
    if i <= member:
        group += 1
        member = 0

print(group)