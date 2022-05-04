x,y = input().split()

rx = ''.join(reversed(x))
ry = ''.join(reversed(y))

rx = int(rx)
ry = int(ry)


lst = list(reversed(str(rx+ry)))

print(ans)


## 이렇게 쉬운 방법을 두고 난 무엇을 했늑ㄴ가...

x, y = map(str, input().split())
sum = str(int(x[::-1]) + int(y[::-1]))
print(int(sum[::-1]))