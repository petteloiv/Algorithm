# 1~10까지의 정수를 항목으로 갖는 리스트 객체 
# filter 함수
# 람다식 이용 
# 짝수만을 선택해 리스트 반환 

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even(i):
    false = lambda i : i%2 == 0 
    return false

result = filter(even, a)

print(list(result))