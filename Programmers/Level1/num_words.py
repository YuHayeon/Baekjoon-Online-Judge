# https://programmers.co.kr/learn/courses/30/lessons/81301
# 프로그래머스 LEVEL 1 - 숫자 문자열과 영단어
# 2021 카카오 채용연계형 인턴십

dic = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def solution(s):
    answer = ""
    alpha = ""

    for i in s:
        if i.isnumeric():
            answer += str(i)
        else:
            alpha += i
        if dic.get(alpha):
            answer += dic[alpha]
            alpha = ""

    answer = int(answer)
    return answer