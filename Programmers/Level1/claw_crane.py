# https://programmers.co.kr/learn/courses/30/lessons/64061
# 프로그래머스 LEVEL 1 - 크레인 인형뽑기 게임
# 2019 카카오 개발자 겨울 인턴십

def solution(board, moves):
    basket = []
    answer = 0

    for num in moves:
        num -= 1
        for row in board:
            if row[num] != 0:
                if basket and basket[-1] == row[num]:
                    answer += 2
                    basket.pop()
                    row[num] = 0
                else:
                    basket.append(row[num])
                    row[num] = 0
                break

    return answer