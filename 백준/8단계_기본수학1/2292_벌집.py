# 6의 배수대로 숫자 커짐 ..

# 주어진 방
n = int(input())

# 각 벌집 가장 끝 숫자
beenum = 1

# 지나가는 벌집
hive = 1

while n > beenum:
        beenum += hive * 6
        hive += 1

print(hive)


