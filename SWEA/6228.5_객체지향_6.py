# Shape를 부모클래스, Square 자식 클래스 
# Square 클래스 = length 필드 가진다 ... 
# Shape 클래스 area 메서드 0 반환
# Square에서 오버라이딩 


class Shape:
    def __init__(self,length):
        self.length = length 

    def area(self):
        return 0 

class Square(Shape):

    def area(self):
        return f'정사각형의 면적: {self.length * self.length}'

s1 = Square(3)
print(s1.area())