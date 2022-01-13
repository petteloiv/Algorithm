user1 = input(홍길동) # 이름 변수로 저장
user2 = input(이순신)

game1 = input(가위) # 동작 변수로 저장
game2 = input(바위)

def game(game1, game2):  # 각 유저의 입력값을 비교해야하기 때문에 매개변수를  def () : 로 선언
    if (game1 == game2):   # 가위바위보의 우승 조건을 if와 elif로 함수 내에서 정의
        print("비겼습니다.")
    elif (game1 == "가위" and game2 == "보"):
        print("가위가 이겼습니다!")
    elif (game1 == "바위" and game2 == "가위"):
        print("바위가 이겼습니다!")
    elif (game1 == "보" and game2 == "바위"):
        print("보가 이겼습니다!")
    elif (game1 == "보" and game2 == "가위"):
        print("가위가 이겼습니다!")
    elif (game1 == "가위" and game2 == "바위"):
        print("바위가 이겼습니다!")
    elif (game1 == "바위" and game2 == "보"):
        print("보가 이겼습니다!")


print(game(game1, game2))