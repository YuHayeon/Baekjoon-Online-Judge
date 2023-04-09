# 18429 : 근손실

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kits = list(map(int, input().split()))

res = []
weight = -k
answer = 0

def back(weight):
    global answer
    
    if len(res)==n:
        answer += 1
        return
    
    for i in range(n):
        kit = kits[i]
        if i in res:
            continue
        
        if weight - k + kit >= 0:
            weight = weight - k + kit
            res.append(i)
            back(weight)
            weight = weight + k - kit
            res.pop()

back(0)
print(answer)
