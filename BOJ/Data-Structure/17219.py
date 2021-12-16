# 17219 : 비밀번호 찾기

import sys

n,m = map(int, sys.stdin.readline().split())
dict = {}

for i in range(n):
    url, password = sys.stdin.readline().split()
    dict[url] = password

for _ in range(m):
    find = sys.stdin.readline().rstrip()
    print(dict.get(find))