# https://programmers.co.kr/learn/courses/30/lessons/12899
# 프로그래머스 LEVEL 2 - 124 나라의 숫자
# 연습문제

def solution(n):
    answer = ''

    while True:
        temp = n % 3

        if temp == 1:
            answer += '1'
        elif temp == 2:
            answer += '2'
        elif temp == 0:
            answer += '4'

        if n//3 == 0 or n/3 == 1:
            break

        if n % 3 == 0:
            n = (n-2)//3
        else:
            n //= 3

    return answer[::-1]
