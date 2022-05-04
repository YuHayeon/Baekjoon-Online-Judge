# 2212 : 센서
# 수신 가능 영역의 최솟값을 구하기 위해 k개의 묶음을 구해야 한다.
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
dist = []
result = 0

# 센서 간의 거리를 구한다.
sensor.sort()
for i in range(1, n):
    dist.append(sensor[i]-sensor[i-1])

# 센서 간의 거리를 구한 것을 내림차순으로 정렬하고 k-1개를 저장한다.
dist_sort = sorted(dist, reverse=True)
dist_sort = dist_sort[:k-1]

first_num = sensor[0]
for i in range(n-1):
    # 센서간의 거리가 정렬한 거리 안에 있을 때 수신 가능 영역을 구해 result에 더해준다.
    if dist[i] in dist_sort:
        dist_sort.remove(dist[i])
        result += sensor[i]-first_num
        first_num = sensor[i+1]
result += sensor[-1]-first_num

print(result)