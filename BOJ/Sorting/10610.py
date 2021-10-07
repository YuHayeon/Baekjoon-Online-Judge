# 10610 : 30

import sys
n = list(map(int,sys.stdin.readline().rstrip().strip()))

if 0 not in n:
    print(-1)
else:
    if sum(n)%3==0:
        n.sort(reverse=True)
        a = ''.join(map(str, n))
        print(a)
    else:
        print(-1)