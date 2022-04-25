
n = int(input())

words = list(input())

words_len = len(words)

for i in range(n-1):
    wordss = list(input())
    for j in range(len(words)):
        if words[j] != wordss[j]:
            words[j] = '?'

print(''.join(words))