# queue 쓰면 풀 수 있다
# dfs bfs 안쓰고도 가느ㅜㅇ ...

import sys
sys.stdin=open("input.txt")

# def Cycle(lst):
#     for i in range(1,6):
#         a = lst.pop(0) - i
#         if a < 0 :
#             a = 0
#             lst.append(a)
#             break
#         lst.append(a)
#     return lst

for tc in range(1,11):
    # 테스트케이스
    T = int(input())
    numbers = list(map(int, input().split()))

    # 시작할 숫자
    i = 1
    # print(numbers)
    # 디버거 돌린 결과 while문과 i값 증가 조건 하나 빠트린게 문제였음
    while numbers[-1] != 0:
        if i > 5:
            # 범위 벗어나면 다시 처음으로 돌려주기
            i = 1
            # a값 설정 (맨 앞 값 - 사이클 번호)
            a = numbers.pop(0) - i
            # a가 0 보다 작거나 0일때 / 끝내기
            if a <= 0:
                a = 0
                numbers.append(a)
                break
            else :
                numbers.append(a)
                i += 1
        # 1 ~ 5 돌고있을 때 ,, 사이클 리셋 빼고는 나머지 다 같게 설정
        else:
            # 여기서 인덱스 에러가 난다 ㅠㅠㅠㅠ => 처음 while문 조건을 while numbers.pop() != 0 으로 설정해서 값이 하나씩 빠지는 중이었다..
            a = numbers.pop(0) - i
            if a <= 0:
                a = 0
                numbers.append(a)
                break
            else :
                numbers.append(a)
                i += 1



    numbers = ' '.join(map(str, numbers))
    print(f'#{tc} {numbers}')