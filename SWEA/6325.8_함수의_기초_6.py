# 정렬된 숫자를 가진 리스트 
# (정렬되어있지 않으면 sorted() 사용)
# 특정 숫자 찾는 함수 정의 
# 임의의 숫자 포함 여부 출력 프로그램 작성 

# trial 1 
# 장렬하게 실패 

# def find_num(num): 
#     # 리스트 num을 순회
#     is_in = ''
#     for i in num:
#         # 특정 숫자 찾기
#         if 5 in num:
#             is_in += '5 => True'
#         else: 
#             is_in += '5 => False'
#         if 10 in num:
#             is_in += '10 => True'
#         else: 
#              is_in += '10 => False'
#     return 

# print(find_num([2, 4, 6, 8, 10]))

# output 
# [2, 4, 6, 8, 10]
# 5 => False
# 10 => True



# trial 2 
# Hint
# 함수에 매개변수 두개 이상 들어갈 수도 있다는 걸 기억해라...
# 변수와 리스트 주고 비교하기 
# 두 값을 한번에 안내도 된다
# 프린트 두번 하면 됨 

def find_num(value, list):
    answer = ''
    if value in list:
        answer += f'{value} => True'
    else: 
        answer += f'{value} => False'
    return answer

print([2, 4, 6, 8, 10])
print(find_num(5, [2, 4, 6, 8, 10]))
print(find_num(10, [2, 4, 6, 8, 10]))

#trial 3 
# for문 활용해보기
# 일단 실패 .. 

# def find_num(value, list):
#     answer = ''
#     for i in list:
#         if value == i:
#             answer = f'{value} => True'
#         else: 
#             answer = f'{value} => False'
#     return answer

# print([2, 4, 6, 8, 10])
# print(find_num(5, [2, 4, 6, 8, 10]))
# print(find_num(10, [2, 4, 6, 8, 10]))
        