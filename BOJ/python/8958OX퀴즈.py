end = int(input())
score = []
for i in range(end):
    result = input()
    count,num = 0, 0
    for j in result:
        if j=="O":
            count=count+1
            num=num+count
        if j=="X":
            count=0
    score.append(num)

for k in score:
    print(k)