# 11723 : 집합

import sys

dict = {}
t = int(sys.stdin.readline())

for num in range(t):
    op = sys.stdin.readline().rstrip()

    if op == 'all':
        for i in range(1, 21):
            dict[i] = i

    elif op == 'empty':
        dict = {}

    else:
        op, num = op.split()
        num = int(num)
        if op == 'add':
            dict[num] = num
        elif op == 'remove':
            if dict.get(num)==num:
                del dict[num]
            else:
                continue
        elif op == 'check':
            if dict.get(num)==num:
                print(1)
            else:
                print(0)
        elif op == 'toggle':
            if dict.get(num)==num:
                del dict[num]
            else:
                dict[num]=num