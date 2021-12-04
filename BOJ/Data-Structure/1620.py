# 1620 : 나는야 포켓몬 마스터 이다솜

import sys

n, m = map(int, sys.stdin.readline().split())
pokemon = {}

def get_key(val):
    for key, value in pokemon.items():
        if val == value:
            return key


for i in range(1, n+1):
    temp = sys.stdin.readline().rstrip()
    pokemon[str(i)] = temp
    pokemon[temp] = str(i)


for _ in range(m):
    find = sys.stdin.readline().rstrip()
    print(pokemon[find])
