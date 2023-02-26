# 2563 : 색종이

import sys
input = sys.stdin.readline

n = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]
answer = 0

for i in range(n):
    w, h = map(int, input().split())
    for i in range(w, w+10):
        for j in range(h, h+10):
            paper[i][j] = 1
for p in paper:
    answer += sum(p)

print(answer)