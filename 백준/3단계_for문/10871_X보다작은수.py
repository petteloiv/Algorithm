# 첫째 줄 N X 
# 둘째 줄 수열 A 이루는 정수 N개 

# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. 
# X보다 작은 수는 적어도 하나 존재한다.

# for, if 동시 사용 

n, x = input().split()
n = int(n)
x = int(x)


a = list(map(int, input().split()))

small = ''
for i in range(0,n):
    if a[i] < x :
        small += str(a[i]) + ' '
print(small)