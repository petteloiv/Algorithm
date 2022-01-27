# 부모클래스 Person
# 자식 클래스 Male, Female
# Person getGender 메서드 - "Unknown" 반환 
# Male, Female에서 Male, Female값 반환하는 메서드로 오버라이딩 

class Person:
    def __init__(self):
        pass

    def getGender(self):
        return "Unknown"

class Male(Person):

    def getGender(self):
        return "Male"

class Female(Person):

    def getGender(self):
        return "Female"

m1 = Male()
print(m1.getGender())
f1 = Female()
print(f1.getGender())