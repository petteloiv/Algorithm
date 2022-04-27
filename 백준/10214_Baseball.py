T = int(input())

for tc in range(1,T+1):
    yonsei = 0
    korea = 0
    for i in range(9):
        y, k = map(int, input().split())
        yonsei += y
        korea += k

    if yonsei > korea:
        print("Yonsei")
    elif korea > yonsei:
        print("Korea")
    else:
        print("Draw")