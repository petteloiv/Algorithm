# ----문제 정의 -----# 
# 숫자 하나 누른 다음에 금속핀 있는 곳까지 시계방향으로 돌려야한다
# 누르면 처음위치로 돌아감 ...
# 다음 숫자 누르려면 처음 위치에서 다시 돌려야한다..

# 1 누를때 걸리는 시간 2초 
# 단어의 길이 2<=word<=15 

# ---------------- 알고리즘 풀이 --------------# 

# 1 - 2 
# 2 ABC -3 
# 3 DEF -4
# 4 GHI -5
# 5 JKL -6
# 6 MNO -7
# 7 PQRS -8
# 8 TUV -9 
# 9 WXYZ -10 
# 0 - 11 

word = list(" ".join(input()))

cnt = 0

for i in range(len(word)):
    if word[i] in 'ABC':
        cnt+=3
    elif word[i] in 'DEF':
        cnt+=4
    elif word[i] in 'GHI':
        cnt+=5
    elif word[i] in 'JKL':
        cnt+=6
    elif word[i] in 'MNO':
        cnt+=7
    elif word[i] in 'PQRS':
        cnt+=8
    elif word[i] in 'TUV':
        cnt+=9
    elif word[i] in 'WXYZ':
        cnt+=10

print(cnt)