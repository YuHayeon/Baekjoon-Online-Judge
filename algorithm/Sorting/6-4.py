# Sorting
# 6-4 두 배열의 원소 교체

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

sum = 0
for i in range(n-k):
    sum += a[i]
for i in range(k):
    sum += b[i]

print(sum)