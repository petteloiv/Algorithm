# 먹어야 할 음식 N 방송 중단된 시점 K초 이후
# 각 음식 먹는데 일정 시간 소요
# 1번 음식부터 ~ 번호 순서대로 음식
# 마지막 번호 후에는 다시 1번
# 1초 동안 섭취 -> 다음 음식 (음식 -= 1)
# 몇 번 음식부터 먹으면 되는가? 더 먹을 음식 없으면 -1

def solution (food_times, k):
    now = 0
    while k != 0:
       if food_times[now] >= 1:
           food_times[now] -= 1
           if now == len(food_times)-1:
               now = 0
               k -= 1
           else:
               now += 1
               k -= 1
       else:
           if now == len(food_times) -1:
               now = 0
           else:
               now += 1

    if food_times[now+1] >= 1:
        return now+1
    else:
        return -1


print(solution([3, 1, 2], 5))
