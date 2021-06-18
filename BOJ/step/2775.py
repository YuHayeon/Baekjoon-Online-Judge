end = int(input())

for i in range(end):
    k = int(input())
    n = int(input())
    num=0
    if n==1: k=1
    for a in range(1,n+1):
        for b in range(1,k+1):
            for c in range(1,b+1):
                num=num+c
            print(num)
