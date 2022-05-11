import sys
sys.stdin=open('input.txt')

n, m = map(int, input().split())
pokemons = [input() for _ in range(n)]
quiz = list(input() for _ in range(m))


for i in quiz:
    if i.isalpha() == 1:
        print(pokemons.index(i) + 1)
    else:
        i = int(i)
        print(pokemons[i-1])
