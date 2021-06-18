n,m,k = input().split()
n = int(n)
m = int(m)
k = int(k)
#n, m, k = map(int, input().split())

num = list(map(int, input().split()))

"""
num.sort()
a = num[n-1]
b = num[n-2]
"""

a = max(num)
num.remove(a)
b = max(num)
result = 0

while (True):

    for i in range(k):
        result = result + a
        m=m-1
    if m <= 0: break

    result = result + b
    m=m-1
    if m <= 0: break

print(result)
