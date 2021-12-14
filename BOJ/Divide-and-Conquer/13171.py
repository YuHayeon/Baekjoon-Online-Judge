# 13171 : A

import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

mod = 1000000007
ans = 1

while b:
    if b % 2 == 1:
        ans = ans * a % mod
    a = (a*a) % mod
    b = b//2

print(ans)