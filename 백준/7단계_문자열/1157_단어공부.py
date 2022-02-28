# 단어 입력 받기
word = input()
# 전체 대문자로 변환
word = word.upper()

words = list(set(word))
# print(words)

cnt = []
for i in words:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(words[(cnt.index(max(cnt)))])



