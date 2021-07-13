# Sorting
# 6-3 성적이 낮은 순서로 학생 출력하기

end = int(input())
grade = {}

for i in range(end):
    n, g = input().split()
    grade.setdefault(n, int(g))

sort = sorted(grade.items(), key = lambda x : x[1])

for item in sort:
    print(item[0], end=' ')