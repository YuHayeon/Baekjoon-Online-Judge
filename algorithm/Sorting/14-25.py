# 14-25 실패율

def solution(n, stages):
    count = [0] * 501
    fail = {}
    answer=[]

    for s in stages:
        count[s] += 1

    total = sum(count)
    for i in range(1, n+1):
        if total == 0:
            fail[i] = 0
        else:
            fail[i] = count[i] / total
        total -= count[i]
    print(fail)
    fail = sorted(fail.items(), key = lambda x : x[1], reverse = True)
    for items in fail:
        answer.append(items[0])
    return answer

N = 4
stages = [4, 4, 4, 4, 4]


print(solution(N,stages))