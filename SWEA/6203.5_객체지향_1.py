class Student : 
    def __init__(self, kor, eng, math):
        self.__kor = kor
        self.__eng = eng
        self.__math = math
        
    @property 
    def kor(self):
        return self.__kor
    
    @property 
    def eng(self):
        return self.__eng
    
    @property
    def math(self):
        return self.__math
    
    def total_grade(self):
        return "국어, 영어, 수학의 총점 : {0}".format(self.__kor + self.__eng + self.__math)

data = list(map(int, input().split(','))) 
students_list = Student(data[0], data[1], data[2]) 
print(students_list.total_grade())

