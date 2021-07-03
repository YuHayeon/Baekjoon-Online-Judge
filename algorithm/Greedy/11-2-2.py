# 11-2 : 곱하기 혹은 더하기

a = list(input())

result = int(a[0])

for i in range(1, len(a)):
    a[i] = max(int(a[i-1])+int(a[i]), int(a[i-1])*int(a[i]))

print(a[len(a)-1])