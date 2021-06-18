n = int(input())
i = 1

while(True):
    if n<=i:break
    n=n-i
    i+=1

if (i%2==1):
    print("%d/%d"%(i-n+1,n))
else:
    print("%d/%d"%(n,i-n+1))