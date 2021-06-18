a=int(input())*int(input())*int(input())

result = str(a)

for i in range(0,10):
    count=0
    for k in result:
        if i==int(k):
            count=count+1
    print (count)