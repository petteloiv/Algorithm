# 학생의 점수 나타내는 리스트 
# while문과 리스트 객체의 pop() 이용해 
# 80점 이상 점수들의 총합 

# 리스트 객체의 pop()가 뭔지 모르겠다.. 
# 종료 조건 설정 필요! 

# trial 1
# output 도출 안되는 문제 발생 .. 
grades = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
total = 0

for i in grades:
    while i <= len(grades):
        total += i 
        print(total) 

# pop() 함수 
# 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다! 
# 정답 코드 참고 

a=[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
b=0

while len(a)>0:
    i= a.pop()
    if i >=80:
        b +=i

# 리스트의 길이가 0 이상일때 ... 
# i = a.pop()
# i의 값이 80이상일때만 b에 저장 

