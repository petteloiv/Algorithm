# Quadrant n == 제 n 사분면
# x,y 둘 다 양수 1사분면
# x<0 2사분면
#둘다 음수 3사분면
#y<0 4사분면

x = int(input())
y = int(input())

if x > 0:
    if y < 0:
        print(4)
    else:
        print(1)
else:
    if y < 0:
        print(3)
    else: 
        print(2)
