# 18258 : 큐2

from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    full_cmd = sys.stdin.readline().split()
    cmd = full_cmd[0]

    if cmd == 'push':
        queue.append(int(full_cmd[1]))
    
    elif cmd == 'pop':
        if queue==deque([]):
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    
    elif cmd == 'size':
        print(len(queue))

    elif cmd == 'empty':
        if queue == deque([]):
            print(1)
        else:
            print(0)

    elif cmd == 'front':
        if queue == deque([]):
            print(-1)
        else: print(queue[0])
    
    elif cmd == 'back':
        if queue == deque([]):
            print(-1)
        else: print(queue[-1])