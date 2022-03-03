num = list(map(int, input()))



num.sort()
# print(num)

result = ''.join(map(str,num))

print(result[::-1])