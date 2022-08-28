# 알파벳 대문자 & 숫자(0~9) 로만 구성된 문자열
# 모든 알파벳 오름차순으로 정렬해 이어서 출력
# 그 뒤에 모든 숫자 더한 값 이어서 출력

n = input()
word = []
sum = 0

for i in n:
    if i.isdecimal() == False:
        word.append(i)
    else:
        sum += int(i)

word.sort()
word.append(str(sum))

print(''.join(word))