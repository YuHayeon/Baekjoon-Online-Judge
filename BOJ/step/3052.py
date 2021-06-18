num = set()

for i in range(0,10):
    x = int(input())
    num.add(x%42)

print(len(num))