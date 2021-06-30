# Binary-Search
# 7-3 떡볶이 떡 만들기

n, m = map(int, input().split())
a = list(map(int, input().split()))

l = max(a)
while True:
    result = 0
    for i in a:
        if i-l > 0:
            result += i-l
        else:
            result += 0
    if result >= m:
        print(l)
        break
    l -= 1