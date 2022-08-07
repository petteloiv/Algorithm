# 볼링공 N개 / 순서대로 번호 부여 / 같은 무게여도 다른 공으로 간주
# 두 사람이 볼링공을 고르는 경우의 수
# 서로 무게 다르게 고를 수 있는 볼링공 번호의 조합 .... 의 수 / 사람은 구분 X

# 볼링공 1차 선택 후 해당 볼링공 이후 번호 비교하면서 같은 무게 제외하고 + 1

n, m = map(int, input().split())
ball = list(map(int, input().split()))

case = 0

for i in range(n-1):
    for j in range(i+1, n):
        if ball[i] != ball[j]:
            case += 1

print(case)