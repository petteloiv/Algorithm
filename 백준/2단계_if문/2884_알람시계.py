# 45분 일찍 알람 설정하기
# 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것.. 
# 24시간제 ... 0:0 ~ 23:59
# 시간 분 <- 이렇게 출력 

H, M = input().split()
H = int(H)
M = int(M)


if M >= 45 :
    M = M-45
    print("{} {}".format(H, M))
else:
    M = M + 60 - 45
    if H == 0:
        H = 24 
    print("{} {}".format(H-1, M))
