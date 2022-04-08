import sys
sys.stdin=open('input.txt')


N = int(input())
words = [input() for _ in range(N)]

wrong = 0

for word in words:
    if len(word) <= 2:
        pass
    else:
        alpha = []
        for i in range(len(word)):
            if word[i] not in alpha:
                alpha.append(word[i])
            else:
                if word[i-1] == word[i]:
                    continue
                else:
                    wrong += 1
                    break

print(N-wrong)