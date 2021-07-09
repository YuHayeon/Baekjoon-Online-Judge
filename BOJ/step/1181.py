# 1181 : 단어 정렬

import sys
n = int(sys.stdin.readline().rstrip())
word = {(sys.stdin.readline().rstrip()) for i in range(n)}
word = sorted(word, key = lambda x : (len(x), x))
sys.stdout.write("\n".join(word))