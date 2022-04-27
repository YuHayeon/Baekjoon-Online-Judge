# 1969 : DNA

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna_list = []
result = [[] for _ in range(m)]
ans = ''
distance = 0

for _ in range(n):
    string = input().rstrip()
    dna_list.append(string)

for i in range(m):
    count = {}
    for dna in dna_list:
        if dna[i] in count.keys():
            count[dna[i]] += 1
        else:
            count[dna[i]] = 1

    for key, value in count.items():
        if max(count.values()) == value:
            result[i].append(key)
    result[i].sort()

    ans += result[i][0]
    distance += n-max(count.values())

print(ans)
print(distance)