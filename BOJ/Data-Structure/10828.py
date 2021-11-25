# 10828 : 스택

import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    full_cmd = sys.stdin.readline().rsplit()
    cmd = full_cmd[0]

    if cmd == 'push':
        stack.append(int(full_cmd[1]))

    elif cmd == 'pop':
        if stack==[]:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()

    elif cmd == 'size':
        print(len(stack))
    
    elif cmd == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)

    elif cmd == 'top':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])