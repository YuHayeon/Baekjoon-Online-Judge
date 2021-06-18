n, m = map(int, input().split())
a = []
for i in range(n):
    num = list(map(int, input().split()))
    """
    min_value = min(num)
    result = max(result, min_value)
    """
    a.append(min(num))

print(max(a))