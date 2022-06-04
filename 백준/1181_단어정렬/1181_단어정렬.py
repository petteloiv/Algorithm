import sys
sys.stdin=open('input.txt')

N = int(input())
arr = list(input() for _ in range(N))
# print(arr)
words = list(set(arr))
# print(words)
n = len(words)


# 버블 1차 -> 길이 비교해서 변경

for i in range(n):
    for j in range(0,n-i-1):
        if len(words[j+1]) < len(words[j]):
            words[j], words[j+1] = words[j+1], words[j]
    # print(words)

# 버블 2차 -> 길이 같으면 사전순으로

for i in range(n):
    for j in range(0, n-i-1):
        if len(words[j]) == len(words[j+1]):
            # 알파벳이 같으면 그 다음 알파벳 확인..
            for i in range(len(words[j])):
                if words[j][i] > words[j+1][i]:
                    words[j], words[j+1] = words[j+1], words[j]
                    break
    # print(words)

# 출력
for i in words:
    print(i)