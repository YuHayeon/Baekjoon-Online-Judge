# 11866 : 요세푸스 문제 0

from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

q = deque([i for i in range(1, n + 1)])
answer = []
i = 1

if k == 1:
    answer = [str(i) for i in range(1, n + 1)]

else:
    while len(q) != 1:
        if i == k:
            answer.append(str(q.popleft()))
            i = 1
        q.append(q.popleft())
        i += 1

    answer.append(str(q.popleft()))

print("<" + ", ".join(answer) + ">")
