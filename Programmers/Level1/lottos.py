# https://programmers.co.kr/learn/courses/30/lessons/77484
# 프로그래머스 LEVEL 1 - 로또의 최고 순위와 최저 순위
# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)

def solution(lottos, win_nums):

    top, low = 1, 7

    for num in lottos:
        if num == 0:
            continue

        if num in win_nums and 1 <= low-1 <= 6:
            low -= 1
        elif 1 <= top+1 <= 6:
            top += 1

    if low == 7:
        low = 6

    answer = [top, low]
    return answer