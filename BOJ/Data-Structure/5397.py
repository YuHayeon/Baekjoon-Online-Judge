# 5397 : 키로거

import sys
t = int(sys.stdin.readline())

for _ in range(t):
    string = sys.stdin.readline().strip()
    left, right = [], []

    for s in string:
        if s == '<':
            if left:
                right.append(left.pop())
        elif s == '>':
            if right:
                left.append(right.pop())
        elif s == '-':
            if left:
                left.pop()
        else:
            left.append(s)

    ans = ''.join(left)+''.join(right[::-1])
    print(ans)