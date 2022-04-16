# 10815 : 숫자 카드

N = int(input())
have_card = list(map(int, input().split()))
M = int(input())
total_card = list(map(int, input().split()))
result = [0 for _ in range(M)]

have_card.sort()


def binary(array, start, end, target):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return True
        if array[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return False


start = 0
for i in range(M):
    if binary(have_card, start, N-1, total_card[i]):
        result[i] = 1

print(*result)