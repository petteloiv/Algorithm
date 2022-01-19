word = input(eye) # 단어를 문자열로 입력


def Palindrome(word):
    correct = word[::-1]   # 입력한 단어를 거꾸로 뒤집어 저장하는 변수
    return correct


if (word == Palindrome(word)):
    print(Palindrome(word))
    print("입력하신 단어는 회문(Palindrome)입니다.")

else:
    print(Palindrome(word))
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")