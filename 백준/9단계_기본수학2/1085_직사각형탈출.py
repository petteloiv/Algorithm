# 문제 
# 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 
# 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

# 주어지는 것
# x, y, w, h 

# trial 1 -solved 

# place = input()
# ps = place.split()
# smallest = []

# x = int(ps[0])
# y = int(ps[1])
# w = int(ps[2])
# h = int(ps[3])

# smallest.append(w-x)
# smallest.append(h-y)
# smallest.append(x-0)
# smallest.append(y-0)
# print(min(smallest))


# trial 2 -solved

# place = input()
# ps = place.split()

# x = int(ps[0])
# y = int(ps[1])
# w = int(ps[2])
# h = int(ps[3])

# smallest = [w-x, h-y, x-0, y-0]
# print(min(smallest))


# trial 3 - solved

# 좌표값들 입력받기
place = input()

# 문자열 -> 숫자로 변환하고 리스트로 만들기
ps = list(map(int, place.split()))

# 각 위치에 해당하는 값 할당
x, y, w, h = ps[0], ps[1], ps[2], ps[3]

# 직사각형 경계까지 가는 값들 중 가장 작은 값 출력
smallest = [w-x, h-y, x-0, y-0]
print(min(smallest))



