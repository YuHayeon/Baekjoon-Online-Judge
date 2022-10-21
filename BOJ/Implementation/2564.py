# 2564 : 경비원

import sys
input = sys.stdin.readline

width, height = map(int, input().split())

n = int(input())
janitors = []

for _ in range(n):
    position, x = map(int, input().split())
    janitors.append((position, x))

me_position, me_x = map(int, input().split())

result = 0
for position, x in janitors:
    distance = 0
    diff_position = abs(me_position-position)

    if diff_position == 0:
        distance = abs(me_x-x)
    elif (me_position == 2 and position == 3) or (me_position == 3 and position == 2):
        distance = x+(height-me_x) if position == 2 else me_x+(height-x)
    elif diff_position == 3:
        distance = width-x+me_x if position == 1 else width-me_x+x
    elif diff_position == 2:
        distance = x+me_x if (position == 1 or position == 3) else width+height-x-me_x
    else:
        distance = min(height+height-x-me_x+width, x+me_x+width) if (position == 3 or position == 3) else min(width+width-x-me_x+height, x+me_x+height)

    result += distance

print(result)


