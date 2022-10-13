# https://school.programmers.co.kr/learn/courses/30/lessons/12913
# Programmers LEVEL 2 - 땅따먹기

def solution(land):
    land_len = len(land)
    d = [[0 for _ in range(4)] for _ in range(land_len)]
    for i in range(0, land_len):
        d[i][0] = max(d[i-1][1], d[i-1][2], d[i-1][3]) + land[i][0]
        d[i][1] = max(d[i-1][0], d[i-1][2], d[i-1][3]) + land[i][1]
        d[i][2] = max(d[i-1][1], d[i-1][0], d[i-1][3]) + land[i][2]
        d[i][3] = max(d[i-1][1], d[i-1][2], d[i-1][0]) + land[i][3]
    answer = max(d[-1])
    return answer

land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
solution(land)
