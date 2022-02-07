# 변경해서 입력하는 크로아티아 알파벳 .. 
# dz, lj, nj -> 무조건 하나의 알파벳
# 나머지 -> 한 글자씩 센다 

# trial 1 .. 코드를 이따구로 짜다니 
'''
# 알파벳 소문자, '-', '=' 로만 이루어진 단어 
# 변경된 형태의 알파벳 단어 입력됨
word = input()

# 두개 붙어 있는 알파벳 찾은 후
# len(word) 에서 빼기 ..? 
# -,=가 거슬린다 .. 

# 뺄 갯수의 알파벳.. (두개짜리 or -,=)
m_word = 0 

# 두개씩 붙어있는 알파벳 세기 
# if안에 if 넣으면 아예 첫 단어 없으면 반복문에 안들어가고
# elif로 처리하면 첫번째에서 통과하면 다음 반복문을 안도는 문제 발생 
if 'lj' in word:
    m_word += 1
if 'nj' in word:
    m_word += 1 
if 'dz' in word:
        m_word += 1 

# -,= 처리하기 
for i in word:
    if i == '-':
        m_word += 1
    elif i == '=':
        m_word += 1 

# 전체길이 - 뺄 숫자
print(len(word)-m_word)
'''

# trial 2 

from dataclasses import replace

# 변환되는 알파벳 리스트로 만들기
rp_word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

# rp_word가 word 안에 있으면 '*'로 변경 
# 2글자 -> 1글자
for i in rp_word:
    if i in word:
        word = word.replace(i, '*')
    else:
        continue
print(len(word))