# 1074 : Z

import sys
n, r, c = map(int, sys.stdin.readline().split())
# 증가하면서 구할 값 선언
cnt = 0


def dq(n, r, c, cnt):
    # 배열의 길이
    len = 2**n
    # 배열의 길이 / 2
    half_len = len//2
    
    # 배열의 길이가 2라면(2**1)
    if n == 1:
        # 왼쪽 위
        if r == 0 and c == 0:
            cnt += 0
        # 오른쪽 위
        elif r == 0 and c == 1:
            cnt += 1
        # 왼쪽 아래
        elif r == 1 and c == 0:
            cnt += 2
        # 오른쪽 아래
        elif r == 1 and c == 1:
            cnt += 3
        return cnt
    
    # 배열의 길이가 2가 아니라면 (재귀)
    else:
        # 만약 배열을 4등분 했을 때 r,c가 왼쪽 위에 속한다면 왼쪽 위 배열만 활용
        if r < half_len and c < half_len:
            return dq(n-1, r, c, cnt)

        # 만약 배열을 4등분 했을 때 r,c가 오른쪽 아래 속한다면 cnt는 전체중의 3/4 값을 더함
        if r >= half_len and c >= half_len:
            cnt += (len**2)//4 * 3
        # 만약 배열을 4등분 했을 때 r,c가 왼쪽 아래 속한다면 cnt는 전체의 1/2 값을 더함
        elif r >= half_len and c < half_len:
            cnt += (len**2)//2
        # 만약 배열을 4등분 했을 때 r,c가 오른쪽 위에 속한다면 cnt는 전체의 1/4 값을 더함
        elif r < half_len and c >= half_len:
            cnt += (len**2)//4
        # 다음 재귀를 위한 r,c 값 조정. 배열을 4등분 했을 때 r,c 값을 1/4 범위로 조정함
        if r-(2**(n-1)) >= 0:
            r = r-(2**(n-1))
        if c-(2**(n-1)) >= 0:
            c = c-(2**(n-1))
        # 재귀함수 호출
        return dq(n-1, r, c, cnt)


print(dq(n, r, c, cnt))
