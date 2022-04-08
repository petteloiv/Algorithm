
import sys
sys.stdin=open('input.txt')

t, m = map(int, input().split())
n = int(input())

x = (m+n) // 60
nm = (m+n) % 60

if t+x >=24:
    nt = t+x-24
else:
    nt = t+x

print(f'{nt} {nm}')