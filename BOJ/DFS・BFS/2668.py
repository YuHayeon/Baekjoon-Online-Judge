# 2668 : 숫자고르기

# 방향 그래프에서 사이클 판별하기

import sys

n = int(sys.stdin.readline())
d = [[] for _ in range(n+1)]
ans = []
visited = [0]*(n+1)
for i in range(1, n+1):
    d[int(sys.stdin.readline())].append(i)

def dfs(start, here):
    # 만약 노드를 방문하고
    if visited[here] == 1:
        # 방문한 노드와 현재 노드가 같다면
        if start == here:
            # 사이클이 형성된 것이므로 True
            return True
    
    # 방문처리
    visited[here] = 1

    # 해당 노드와 연결된 노드를 탐색
    for i in d[here]:
        if dfs(start, i):
            # True라면 사이클이 형성된 것이므로 배열에 넣기
            ans.append(i)
            return True

for i in range(1, n+1):
    dfs(i, i)
print(len(ans))
ans.sort()
for a in ans:
    print(a)
