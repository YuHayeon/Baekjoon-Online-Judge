#Implementation
#4-2 왕실의 나이트

n = input()
m = [[2,-1], [2,1], [-2,-1], [-2,1], [1,2], [1,-2], [-1,-2], [-1,2]]
count = 0

for i in m:
    if ((ord(n[0])+i[0])>96 and (int(n[1])+i[1])>0 and (ord(n[0])+i[0])<105 and (int(n[1])+i[1])<9):
        count = count+1

print(count)