tup = ('Forest', 'Ocean', 'Mountain', 'Plain')

num = int(input())
lst = [1, 2, 3, 4]
if num in lst:
    print(tup[num-1])
else:
    print('Input Error')