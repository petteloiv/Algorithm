a, m = map(int, input().split())

if a + m < 0 or a-m < 0 or (a + m)%2:
    print(-1)
else:
    f = (a - m)//2 + m
    s = a - f
    print(f'{f} {s}')