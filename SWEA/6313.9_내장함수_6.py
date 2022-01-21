# ascii 코드 값 입력받아 문자를 확인하는 코드 

a = int(input())
def function(a):
    alphabet = chr(a)
    sentence = "ASCII {0} => {1}".format(a, alphabet)
    return sentence

print(function(a))


# chr() == 숫자 -> 문자
# ord() == 문자 -> 숫자