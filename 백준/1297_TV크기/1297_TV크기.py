

import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(1,T+1):
    D, H, W = map(int, input().split())

    # 1. 가로세로 비율 * 2 한 값 구하기
    num = (H/(H+W))** 2 + (W/(H+W))**2
    x = D**2 *


    # 그냥 대각선 비율 구하면 되는 문제였다 ㅠ