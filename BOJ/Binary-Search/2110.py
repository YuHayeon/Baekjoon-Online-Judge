# 2110 : 공유기 설치

import sys

n, c = map(int, sys.stdin.readline().split())
home = [int(sys.stdin.readline()) for _ in range(n)]
home.sort()

start = 1
end = home[n-1]-home[0]

while start<=end:
    mid = (start+end) // 2
    cnt = 1
    pre_home = home[0]

    # 공유기 설치
    for i in range(1, n):
        if home[i]-pre_home >= mid:
            cnt += 1
            pre_home = home[i]

    # 설치해야하는 공유기의 개수가 작을 때 -> 간격 넓힘
    if cnt >= c:
        result = mid
        start = mid+1
    # 설치해야하는 공유기의 개수보다 클 때 -> 간격 좁힘
    else:
        end = mid-1

print(result)