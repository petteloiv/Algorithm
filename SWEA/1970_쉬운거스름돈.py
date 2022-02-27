import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1,T+1):
    money = int(input())
    m = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * 8

    for i in range(8):
        if money//m[i] !=0:
            cnt[i] = money//m[i]
            money = money%m[i]
        else:
            continue

    cnt = ' '.join(map(str, cnt))
    print(f'#{tc}')
    print(f'{cnt}')


    # howmany = {50000:0, 10000:0, 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0}
    #
    # while money != 0:
    #     if money >= 50000:
    #         a = money // 50000
    #         howmany[50000] = a
    #         money = money - 50000 * a
    #     elif 10000<= money < 50000:
    #         b = money // 10000
    #         howmany[10000] = b
    #         money = money - 10000 * b
    #     elif 5000<= money < 10000:
    #         c = money // 5000
    #         howmany[5000] = c
    #         money = money - 5000 * c
    #     elif 1000<= money < 5000:
    #         d = money // 1000
    #         howmany[1000] = d
    #         money = money - 1000 * d
    #     elif 500<= money < 1000:
    #         e = money // 500
    #         howmany[500] = e
    #         money = money - 500 * e
    #     elif 100<= money < 500:
    #         f = money // 100
    #         howmany[100] = f
    #         money = money - 100 * f
    #     elif 50 <= money < 100:
    #         g = money // 50
    #         howmany[50] = g
    #         money = money - 50 * g
    #     else:
    #         e = money // 10
    #         howmany[10] = e
    #         money = money - 10 * e
    #
    # howmany = ' '.join(map(str,howmany.values()))
    # print(f'#{tc} {howmany}')

