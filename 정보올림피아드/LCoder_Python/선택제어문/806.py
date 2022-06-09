s, a = input().split()

a = int(a)

if s == 'F' and a < 18:
    print("GIRL")
elif s == 'F' and a >= 18:
    print("WOMAN")
elif s == 'M' and a < 18:
    print("BOY")
else:
    print("MAN")