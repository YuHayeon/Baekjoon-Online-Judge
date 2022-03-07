# https://programmers.co.kr/learn/courses/30/lessons/42586
# 프로그래머스 LEVEL 2 - 기능 개발
# 스택/큐

from collections import deque


def solution(progresses, speeds):

    answer = []
    progresses, speeds = deque(progresses), deque(speeds)

    while progresses:
        result = 0

        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            result += 1

        if result > 0:
            answer.append(result)

        while progresses and progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]

    return answer