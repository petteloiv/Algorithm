count = 0

for i in range(1, 101):
    if i % 3 == 0:
        count += i 
    else:
        continue
print(f'1부터 100사이의 숫자 중 3의 배수의 총합: {count}')