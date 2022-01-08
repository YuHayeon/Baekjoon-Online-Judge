# 9465 : 스티커

import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
	n = int(input())
	sticker = [list(map(int, input().split())) for _ in range(2)]
	d = [[0 for _ in range(n)] for _ in range(2)]
	result = 0

	d[0][0], d[1][0] = sticker[0][0], sticker[1][0]
	if n > 1:
		d[0][1], d[1][1] = d[1][0]+sticker[0][1], d[0][0]+sticker[1][1]

	for i in range(2, n):
		d[0][i] = max(d[1][i-1], d[1][i-2]) + sticker[0][i]
		d[1][i] = max(d[0][i-1], d[0][i-2]) + sticker[1][i]

	result = max(d[0][n-1], d[1][n-1])
	print(result)
