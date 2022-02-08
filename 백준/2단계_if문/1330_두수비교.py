# a,b 공백 한 칸으로 구분 

a, b = input().split()
a = int(a)
b = int(b)

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')