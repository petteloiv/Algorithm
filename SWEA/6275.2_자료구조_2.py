# 리스트 내포 기능 이용
# 문장으로부터 모음 제거 

# trial 1

# a = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

# vowels = 'aeiou'

# for i in a:
#     word = ''
#     if i not in vowels:
#         word += i
#     print(word)
# print(''.join(word))

# 모음 제거까지는 성공했지만 다 하나하나 나오는걸 합치지 못했다 ... 

# cheatted code 

str = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
vowels = list('aeiou')

str_list = [word for word in str if word not in vowels]

print(''.join(str_list))

# trial 2 # 실패. 각각의 리스트로 담긴다 ..

# str = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
# vowels = list('aeiou')

# for i in str:
#     word = []
#     if i not in vowels:
#         word.append(i)
#     print(''.join(str(word)))
