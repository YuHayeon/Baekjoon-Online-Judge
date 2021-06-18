x,y,w,h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)

if x>w: a = x-w
else: a = w-x

if y>h: b = y-h
else: b = h-y

if a>b: print(a)
else: print(b)