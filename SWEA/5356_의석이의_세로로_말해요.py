

import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1,T+1):
    words = [list(map(str,input())) for _ in range(5)]

    new_words = ''
    # 문자열 최대 길이 == 15
    # 열 우선 순회
    for i in range(15):
        # 행은 항상 5개 ~
        for j in range(5):
            try:
                new_words += str(words[j][i])
            except:
                continue

    print(f'#{tc} {new_words}')


