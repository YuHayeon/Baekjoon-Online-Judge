# 2941 : 크로아티아 알파벳

import sys
input = sys.stdin.readline

croatia = ["c=", "c-", "dz=", "d-", 'lj', "nj", "s=", "z="]

string = input().strip()

for alphabet in croatia:
    if alphabet in string:
        string = string.replace(alphabet, 'a')

result = len(string)
print(result)