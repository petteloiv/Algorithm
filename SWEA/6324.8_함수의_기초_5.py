# trial 1 
# 답은 제대로 나오지만 오답 처리됨

# def only_num (list):
#     list = [1, 2, 3, 4, 3, 2, 1]
#     return set(list)

# print(list(only_num()))

# # set() 은 오름차순 정렬... 
# # set 사용할거면 

# numbers = [1, 2, 3, 4, 3, 2, 1]

# print(numbers)
# print(list(set(numbers)))

# #--------------------------------------
# numbers = [1, 2, 3, 4, 3, 2, 1]

# trial 2 
# 1. 리스트 입력 
# 2. 리스트 순회하며  

def only_num(num):
    count = [] 
    for i in num:
        if i in count:
            continue
        else:
             count += [i]                      
    return count

numbers = [1, 2, 3, 4, 3, 2, 1]
print(numbers)
print(only_num(numbers))

# pass 