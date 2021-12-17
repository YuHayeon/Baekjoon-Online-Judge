# 11723 : 집합

import sys
bit = 0
def set_operation(op, num):
    global bit
    if op == 'add':
        bit = bit | (1<<num)
    elif op == 'remove':
        bit = bit & ~(1<<num)
    elif op == 'check':
        if bit & (1<<num) == 0:
            print(0)
        else: print(1)
    elif op == 'toggle':
        bit = bit ^ (1<<num)

t = int(sys.stdin.readline())
for _ in range(t):
    op = sys.stdin.readline().rstrip()

    if op == 'all':
        bit = (1 << 20) -1
    elif op == 'empty':
        bit = 0
    else:
        op, num = op.split()
        set_operation(op, int(num)-1)