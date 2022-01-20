# # 입력된 문자가 대문자 -> 소문자, 소문자 -> 대문자 변경
# # 알파벳 아닐 경우 그냥 출력 
# # 출력 시 아스키코드 함께 출력  

# number = input()
# number_changed = ''

# if number #대문자일경우:
#     number_changed = number.lower
#     print(f'{number}(ASCII: {ord(number)} => {number_changed}(ASCII: {ord(number_changed)}')
# elif number #소문자일경우:
#     number_changed = number.upper
#     print(f'{number}(ASCII: {ord(number)} => {number_changed}(ASCII: {ord(number_changed)}')
# else:
#     print(number)

# 기본 지식이 필요한 문제였다 ... 
# 소문자 96< <123
# 대문자 64< <91

a = input()

if ord(a)>96 and ord(a)<123:
    print(f'{a}(ASCII: {ord(a)}) => {a.upper()}(ASCII: {ord(a.upper())}) ')
elif ord(a)>64 and ord(a)<91:
    print(f'{a}(ASCII: {ord(a)}) => {a.lower()}(ASCII: {ord(a.lower())}) ')
else:
    print(a)

