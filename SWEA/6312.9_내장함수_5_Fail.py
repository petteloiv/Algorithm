# 가변형 인자로 정수 입력
# 곱 반환 
# 1, 2, '4', 3 과 같이 제대로 입력되지 않은 경우
# 예외 처리하는 프로그램 

def function(*num):
    a = 1
    num = int()
    for i in num:
        a *= i
    return a 
    
  
 
try: 
    print(function(1, 2, '4', 3))

except: # 실행이 안 될 경우 
    print('에러발생')

# 가변형 인자 *args
# 키워드형 인자 **kwargs
