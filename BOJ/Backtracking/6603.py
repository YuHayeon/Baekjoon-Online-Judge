# 6603 : 로또

import sys
input = sys.stdin.readline


def lotto(start):
    if len(res) == 6:
        print(' '.join(map(str, res)))
        
    for i in range(start, k):
        if S[i] in res:
            continue
        res.append(S[i])
        lotto(i)
        res.pop()


while True:
    S = list(map(int, input().split()))
    k = S.pop(0)
    if k == 0:
        break
    res = []

    lotto(0)
    print()