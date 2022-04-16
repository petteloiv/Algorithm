

total = 0
total_number = 0

for num in range(1,101):
    if num % 2 != 0:
        total += num
    elif num % 2 == 0:
        total_number += 1

    if num == 100 :
        print(num)
    elif num % 10 == 0:
        print(num, end=", ")
