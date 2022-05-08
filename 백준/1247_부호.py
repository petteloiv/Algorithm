

for tc in range(3):
    n = int((input()))
    num = list(int(input()) for _ in range(n))
    ans = sum(num)
    if ans > 0 :
        print("+")
    elif ans < 0 :
        print("-")
    else:
        print(0)