

import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(1,T+1):
    # float으로 받아오기
    n = float(input())

    # 구하는 방법 ; *2 곱해서 정수부, 소수부로 나눈 후
    # 소수부만 떼서 반복
    # 소수부가 0 되면 정수부 출력
    ans = ''
    while n != 0:
        # 2곱해주기
        c = n*2
        # 정수 부분만 빼서 ans에 더해주기
        ans += str(int(c))
        # 나머지 소수 부분을 n으로 다시 설정
        n = c - int(c)

    # ans 길이가 12 이내라면 그대로 출력
    # 아니라면 overflow 출력
    if len(ans) <= 12:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} overflow')
