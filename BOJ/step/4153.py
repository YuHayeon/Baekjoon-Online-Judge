while(True):
    a, b, c = input().split()
    side = []
    side.append(int(a))
    side.append(int(b))
    side.append(int(c))

    if (side==[0, 0, 0]):
        exit(0)

    num = max(side) ** 2
    side.remove(max(side))
    if (num == (side[0] ** 2) + (side[1] ** 2)):
        print("right")
    else:
        print("wrong")