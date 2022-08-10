# 2644 : 촌수계산

import sys
from collections import deque

input = sys.stdin.readline


def degree_kinship(kinship, person1, person2):
    degree = [0 for _ in range(n+1)]

    q = deque()
    q.append(person1)
    while q:
        v = q.popleft()

        if v == person2:
            return degree[person2]

        for person in kinship[v]:
            if degree[person] == 0:
                degree[person] = 1 + degree[v]
                q.append(person)

    return -1


if __name__ == "__main__":
    n = int(input())
    person1, person2 = map(int, input().split())
    m = int(input())

    kinship = [[] for _ in range(n+1)]

    for _ in range(m):
        parent, child = map(int, input().split())
        kinship[parent].append(child)
        kinship[child].append(parent)

    result = degree_kinship(kinship, person1, person2)
    print(result)
