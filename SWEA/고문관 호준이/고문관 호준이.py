import sys
sys.stdin = open('input.txt')


def f(start, nxt, num):
    global st
    # print(i, start, lst)
    if num == len(nxt):
        if start == ans:
            st = st | {i}
        return

    f(start+nxt[num], nxt, num+1)
    f(start*nxt[num], nxt, num+1)


N = int(input())
for tc in range(1,N+1):
    ans = int(input())
    nxt = list(map(int, input().split()))
    idx = nxt.index(0)
    st = set()

    for i in range(1, N+1):
        nxt[idx] = i
        # nxt =[7, 1, i]
        # f(start, nxt, 0, [])
        rtn = f(nxt[0], nxt[1:], 0)
        # if rtn:
        #     print(rtn)
    print(f'#{tc} {len(st)}')