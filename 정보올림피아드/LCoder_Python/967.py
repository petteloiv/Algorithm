a, b = map(int, input().split())

def check():
   global a,b

   if a > b:
       a = a//2
       b = b*2
   else:
       a = a*2
       b = b//2

check()


print(f'{a} {b}')
