#Sorting
#6-2 위에서 아래로

end = int(input())
num = []

for i in range(end):
    num.append(int(input()))

num.sort()
# num = sorted(num, reverse=True)

for j in range(end-1, -1, -1):
    print(num[j], end=' ')