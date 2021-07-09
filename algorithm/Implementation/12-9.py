# 12-9 : 문자열 압축
import sys

def solution(n):
    r=[]
    end = len(n)
    for i in range(1, end//2+2):
        temp = n[0:i]
        result, count = 0, 1
        for j in range(i, end, i):
            if temp == n[j:j+i]:
                count += 1
            else:
                if count != 1:
                    result += len(str(count))+len(temp)
                    count = 1
                else:
                    result += len(temp)
                    count = 1
            temp = n[j:j+i]
        if count != 1 :
            result += len(str(count))+len(temp)
        else:
            result += len(temp)
        r.append(int(result))
    answer = min(r)
    return answer

print(solution(sys.stdin.readline().rstrip()))