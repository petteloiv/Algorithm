import sys
sys.stdin=open('input.txt')

score = 0

for i in range(1,6):
    score += int(input())

print(score)