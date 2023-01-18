# 정렬 후 큰 숫자부터
# 그 수만큼 그룹구성
# 남은 모험가가 없거나 숫자만큼 담을 수 없으면 끝

n = int(input())

hunter = list(map(int, input().split()))

hunter.sort(reverse=True)
cnt = 0

while len(hunter) > 0 :
        try:
            i = hunter[0]
            del hunter[:i]
            cnt += 1
        except:
            break

print(cnt)
