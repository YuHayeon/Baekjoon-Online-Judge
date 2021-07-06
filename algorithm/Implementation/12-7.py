# 12-7 : 럭키 스트레이트

import sys
n = sys.stdin.readline().rstrip()

num1, num2 = 0, 0
end = len(n)//2
for i in range(end):
    num1 += int(n[i])
    num2 += int(n[i+end])

if num1==num2 :
    print("LUCKY")
else:
    print("READY")