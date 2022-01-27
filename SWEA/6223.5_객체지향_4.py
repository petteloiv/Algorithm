# 반지름 정보를 갖고
# 원의 면적을 계산하는 메서드 갖는 Circle 클래스 정의

# 생성한 객체의 원의 면적 출력하는 프로그램 

class Circle:
    pi = 3.14 

    def __init__(self, r):
        self.r = r 

    def area(self):
        return f'원의 면적: {Circle.pi * self.r * self.r}'

c1 = Circle(2)
print(c1.area())