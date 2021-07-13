# 2108 : 통계학

import sys
from collections import Counter
n = int(sys.stdin.readline().rstrip())
num = [int(sys.stdin.readline().rstrip()) for i in range(n)]

mode = Counter(sorted(num)).most_common(2)
if len(mode) == 1 or mode[0][1] != mode[1][1]:
    many = mode[0][0]
else: many = mode[1][0]

sys.stdout.write(str(round(sum(num)/n))+'\n')
sys.stdout.write(str(sorted(num)[n//2])+'\n')
sys.stdout.write(str(many)+'\n')
sys.stdout.write(str(max(num)-min(num))+'\n')