# 1946 : 신입 사원

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    grades = []

    for _ in range(n):
        grade1, grade2 = map(int, input().split())
        grades.append((grade1, grade2))

    grades.sort()

    min_grade = grades[0][1]
    result = 1
    for i in range(1, n):
        grade = grades[i][1]
        if grade < min_grade:
            min_grade = grade
            result += 1

    print(result)
