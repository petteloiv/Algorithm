# class Student : 
#     def __init__(self, kor, eng, math):
#         self.__kor = kor
#         self.__eng = eng
#         self.__math = math
        
#     @property 
#     def kor(self):
#         return self.__kor
    
#     @property 
#     def eng(self):
#         return self.__eng
    
#     @property
#     def math(self):
#         return self.__math
    
#     def total_grade(self):
#         return "국어, 영어, 수학의 총점 : {0}".format(self.__kor + self.__eng + self.__math)

# data = list(map(int, input().split(','))) 
# students_list = Student(data[0], data[1], data[2]) 
# print(students_list.total_grade())



# 국어, 영어, 수학 점수 입력
# 합계 구하는 객체지향 코드
# 학생 클래스의 객체 -> 생성시 국어, 영어, 수학 점수 저장 
# 총점 구하는 메서드 제공 

class Student: 

    def __init__(self, kor, eng, math):
        # 여기서부터 오류가 난다... 이렇게 저장하는게 아닌가? 
        self.__kor = kor
        self.__eng = eng
        self.__math = math 

    # @property
    # def kor(self):
    #     return self.__kor

    # @property
    # def eng(self):
    #     return self.__eng

    # @property
    # def math(self):
    #     return self.__math


    def total(self):
        total_num = self.__kor + self.__eng + self.__math
        return f'국어, 영어, 수학의 총점:{total_num}'

# 입력받은 input(문자열 형태) => , 기준으로 나눠주고 숫자로 변환하는 과정 필요

score = input().split(',')
s1 = Student(int(score[0]), int(score[1]), int(score[2]))
s1.total()

# 정답 코드 참고 공부 .. 
'''
class Student:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sumScore(self):
        return self.kor + self.eng + self.mat

kor, eng, mat = map(int, input().split(','))
s = Student(kor, eng, mat)
print('국어, 영어, 수학의 총점: {}'.format(s.sumScore()))
'''

# trial 3 - 내 코드를 다시 고쳐보자 

class Student: 

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math 

    def total(self):
        return self.kor + self.eng + self.math

score = input().split(',')
s1 = Student(int(score[0]), int(score[1]), int(score[2]))
# 프린트를 바깥으로 빼야하겠다 .... 코드 안에 넣어서 리턴으로는 답이 안나온다 ㅠㅠ 
print(f'국어, 영어, 수학의 총점: {s1.total()}')

# trial 4 - 다시 속에 코드 넣기 .. 도전 >>> 성공! 

class Student: 

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math 

    def total(self):
        print(f'국어, 영어, 수학의 총점: {(self.kor + self.eng + self.math)}') 

score = input().split(',')
s1 = Student(int(score[0]), int(score[1]), int(score[2]))
print(s1.total())