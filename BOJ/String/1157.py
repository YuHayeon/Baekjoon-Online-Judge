# 1157 : 단어 공부

import sys

string = sys.stdin.readline().strip().upper()
word = list(set(string))
cnt = []

for w in word:
    cnt.append(string.count(w))


if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word[cnt.index(max(cnt))])