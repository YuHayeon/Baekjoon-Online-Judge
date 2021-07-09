# 2750 : 수 정렬하기
import sys
n = int(sys.stdin.readline().rstrip())
num = [(int(sys.stdin.readline().rstrip())) for i in range(n)]
num.sort()
for i in num:
    sys.stdout.write(str(i)+"\n")