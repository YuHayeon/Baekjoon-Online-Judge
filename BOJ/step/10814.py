# 10814 : 나이순 정렬
import sys
n =int(sys.stdin.readline().rstrip())
member = []
for i in range(n):
    member.append(tuple(sys.stdin.readline().split()))
member.sort(key= lambda x : int(x[0]))
for i in member:
    sys.stdout.write(i[0]+" "+i[1]+"\n")