# 가로, 세로 정보 갖고
# 사각형 면적 계산하는 메서드 갖는
# 클래스 Rectangle
# 생성한 객체의 사각형 면적 출력 

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height 

    def area(self): 
        print("사각형의 면적: {}".format(self.width * self.height))

r1 = Rectangle(5, 4)
r1.area()