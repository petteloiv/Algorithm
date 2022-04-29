import sys
sys.stdin=open('24736.txt')


visit = list(map(int, input().split()))
home = list(map(int, input().split()))

visitcnt = 0
homecnt = 0


for i in range(5):
    if i == 0:
        visitcnt += visit[i] * 6
    elif i == 1:
        visitcnt += visit[i] * 3
    elif i == 2 or i == 4:
        visitcnt += visit[i] * 2
    elif i == 3:
        visitcnt += visit[i]

for i in range(5):
    if i == 0:
        homecnt += home[i] * 6
    elif i == 1:
        homecnt += home[i] * 3
    elif i == 2 or i == 4:
        homecnt += home[i] * 2
    elif i == 3:
        homecnt += home[i]


print(f'{visitcnt} {homecnt}')