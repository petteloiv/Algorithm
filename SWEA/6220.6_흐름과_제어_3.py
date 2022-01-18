a = input('영어 알파벳을 입력하십시오: ')

if a.isupper():
    print(f'{a} 는 대문자 입니다.')
else:
     print(f'{a} 는 소문자 입니다.')


# f string 쓴 코드가 오답처리돼서 % formatting 으로 다시 풀었다.

W = input()

if W.isupper():
    print("%s 는 대문자 입니다." %W)
else:
     print("%s 는 소문자 입니다." %W)