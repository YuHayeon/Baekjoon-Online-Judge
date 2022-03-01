# https://programmers.co.kr/learn/courses/30/lessons/67256
# 프로그래머스 LEVEL 1 - 키패드 누르기
# 2020 카카오 인턴십

def distance(prev, now):

    dist = abs(prev-now)

    if prev == -1:
        return distance(0, now) + 1
    if prev == now:
        return 0
    if prev == 0:
        return distance(8, now) + 1
    if now == 0:
        return distance(prev, 8) + 1

    if dist == 1 or dist == 3:
        return 1
    elif dist == 2 or dist == 4 or dist == 6:
        return 2
    elif dist == 5 or dist == 7:
        return 3


def solution(numbers, hand):

    answer = ''
    right, left = -1, -1

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += "L"
            left = num

        elif num == 3 or num == 6 or num == 9:
            answer += "R"
            right = num

        else:
            right_dist = distance(right, num)
            left_dist = distance(left, num)

            if right_dist < left_dist:
                answer += "R"
                right = num
            elif left_dist < right_dist:
                answer += "L"
                left = num
            else:
                if hand == 'right':
                    answer += "R"
                    right = num
                elif hand == 'left':
                    answer += "L"
                    left = num

    return answer