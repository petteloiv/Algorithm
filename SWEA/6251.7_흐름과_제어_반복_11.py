# for문을 이용해 아래와 같이 별 표시
# 
#     *

#    **

#   ***

#  ****

# *****

# 답은 맞게 나오지만 오답으로 처리됨 

blank = 5
for i in range(1,6):
    print("{0}{1}".format((' '*blank),('*'*i)))
    blank -= 1

# 코드 참고 
# {:>5} 사용해 오른쪽 정렬 

# star = '*'
# for i in range(1,6):
#     print(f'{star*i:>5}')

# .format 사용

for i in range(1,6):
    print("{:>5}".format('*'*i))

# % formatting 사용 

for i in range(1,6):
    print("%5s"%('*'*i))