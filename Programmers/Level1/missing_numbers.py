# https://programmers.co.kr/learn/courses/30/lessons/86051
# 프로그래머스 LEVEL 1 - 없는 숫자 더하기
# 월간 코드 챌린지 시즌3

def solution(numbers):
    total = sum([1, 2, 3, 4, 5, 6, 7, 8, 9])
    answer = total-sum(numbers)
    return answer
