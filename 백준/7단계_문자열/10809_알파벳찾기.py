# 알파벳 소분자로만 이루어진 단어 S 
# 각각의 알파벳 .. 
# 단어에 포함되어있는 경우 처음 등장하는 위치 
# 단어에 없으면 -1 출력 

# 알파벳 리스트 
# 카운트 리스트 


word = input()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = []

for i in alpha:
    if i in word:
        count.append(word.index(i))
    else:
        count.append(-1)

count = ' '.join(map(str,count))
print(count)