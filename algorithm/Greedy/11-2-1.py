# 11-2 : 곱하기 혹은 더하기

a = list(input())

result = int(a[0])

for i in range(1, len(a)):
    if int(a[i]) == 0 or int(a[i]) == 1 or int(a[i-1])==0:
        result = result + int(a[i])
    else:
        result = result * int(a[i])

print(result)
