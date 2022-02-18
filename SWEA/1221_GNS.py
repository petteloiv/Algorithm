# ---------- 문제 정의 --------------#
# 숫자 체계가 우리와 다른 어느 행성 있다 ...
# 0~9값 : "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

# 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램 ..

# 오늘 배운 문자열 알고리즘을 사용하지 않았다 ,,
# 첫번째 시도에 통과

# --------------알고리즘 풀이 ------------#

import sys
sys.stdin=open("input.txt")

T = int(input())

for t in range(T):
    tc, n = map(str, input().split())
    n = int(n)
    # 입력값 리스트로 저장
    xxsort = list(map(str, input().split()))

    # 사용하는 ,, 외계 어쩌구 숫자 (문자열이 의미하는 수는 인덱스 번호와 같다)
    space_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # 외계 문자열 -> 숫자로 변환해 넣을 리스트
    yysort = []

    # xxsort의 i번째 값을 space_num에서 찾아 그 값의 인덱스로 새 리스트에 저장
    for i in range(n):
        yysort.append(space_num.index(xxsort[i]))
        # print(yysort)

    # 버블정렬로 풀어보기!!!!
    # 내장함수 쓰지 맛요 ...
    # yysort.sort()
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if yysort[j] > yysort[j+1]:
                yysort[j], yysort[j+1] = yysort[j+1], yysort[j]

    # 전체 리스트 순회
    for i in range(n):
        # 숫자는 0~9까지이므로 범위 지정 .. 전체 리스트 각각의 값이 무엇과 대응되는지 확인
        for j in range(10):
            # yysort의 i번째 값이 j와 같다면 space_num의 j번째에 들어있는 값으로 바꿔서 저장
            if yysort[i] == j :
                yysort[i] = space_num[j]

    # 프린트 하기
    result = str(' '.join(map(str, yysort)))
    print(f'{tc} {result}')





