# https://programmers.co.kr/learn/courses/30/lessons/76501
# 프로그래머스 LEVEL 1 - 음양 더하기
# 월간 코드 챌린지 시즌2

def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer += (-1) * absolutes[i]

    return answer