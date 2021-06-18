count = 0

for i in range(100):
    for j in str(i):
        count = count + int(j)
    print(i+count)
