# ---------문제 정의 -------------#
# N개의 숫자로 이루어진 수열 존재
# 맨 앞 숫자 -> 맨 뒤로 보내기 * M번

# queue 써서 푸는 문제 ..
# front값 빼서 rear에 집어넣기 반복
# enQueue(deQueue())
# 원형큐를 써보고싶은데 잘 모르겠다

# ----------------알고리즘 풀이 --------------#
import sys
sys.stdin=open("input.txt")

# 테케
T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    # m번 반복하면서 맨 앞 값 빼서 맨 뒤에 집어넣기
    for i in range(m):
        num.append(num.pop(0))
    # 맨 앞 값 출력
    print(f'#{tc} {num[0]}')