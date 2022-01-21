# 10830 : 행렬 제곱

import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
mod = 1000
result = [[0 for _ in range(N)] for _ in range(N)]


def divide(matrix, b):

    if b == 1:
        for i in range(N):
            for j in range(N):
                matrix[i][j] %= mod
        return matrix

    elif b == 2:
        result = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    result[i][j] += matrix[i][k] * matrix[k][j]
                result[i][j] %= mod
        return result

    elif b % 2 == 1:
        result = [[0 for _ in range(N)] for _ in range(N)]
        tmp = divide(matrix, b-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    result[i][j] += tmp[i][k] * matrix[k][j]
                result[i][j] %= mod
        return result

    else:
        result = [[0 for _ in range(N)] for _ in range(N)]
        tmp = divide(matrix, b//2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    result[i][j] += tmp[i][k] * tmp[k][j]
                result[i][j] %= mod
        return result


ans = divide(A, B)
for a in ans:
    print(*a)