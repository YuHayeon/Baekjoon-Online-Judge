# Binary-Search
# 7-3 떡볶이 떡 만들기

n, m = map(int, input().split())
a = list(map(int, input().split()))

start = 0
end = max(a)

h = 0
while True:
    if (start >= end):
        break
    result = 0
    mid = (start+end) // 2
    for i in a:
        if i-mid > 0:
            result += i-mid

    if result < m:
        end = mid-1
    else:
        h = mid
        start = mid+1

print(mid)