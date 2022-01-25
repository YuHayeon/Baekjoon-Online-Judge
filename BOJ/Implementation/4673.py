# 4673 : 셀프 넘버

a = [i for i in range(1, 10000)]


def self(n):
    num = list(map(int, str(n)))
    res = n+sum(num)
    if res in a:
        a.remove(res)
        self(res)
    else:
        return


for i in a:
    self(i)
    print(i)
