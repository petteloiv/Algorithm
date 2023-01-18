s = list(map(int, input()))
# print(s)

now = s[0]

for i in range(1, len(s)):
    if now == 0 or s[i] == 0:
        now = now + s[i]
    else:
        now = now * s[i]

print(now)