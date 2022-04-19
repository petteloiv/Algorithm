
while True:
    f, s = map(int, input().split())
    if f == 0 and s == 0:
        break
    else:
        if s % f == 0:
            print('factor')
        elif f % s == 0:
            print('multiple')
        else:
            print('neither')
