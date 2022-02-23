# https://programmers.co.kr/learn/courses/30/lessons/72410
# 프로그래머스 LEVEL 1 - 신규 아이디 추천
# 2021 KAKAO BLIND RECRUITMENT

def solution(new_id):

    # 1단계
    id = new_id.lower()

    # 2단계
    i = 0
    while True:
        if i == len(id):
            break
        if not(id[i].isalnum()) and id[i] != "-" and id[i] != "_" and id[i] != ".":
            id = id.replace(id[i], "")
        else:
            i += 1

    # 3단계
    while ".." in id:
        id = id.replace("..", ".")

    # 4단계
    if id and id[0] == ".":
        id = id.strip(id[0])
    if id and id[-1] == ".":
        id = id.strip(id[-1])

    # 5단계
    if id == "":
        id = "a"

    # 6단계
    if len(id) >= 16:
        id = id[0:15]
        if id[-1] == ".":
            id = id.strip(id[-1])

    # 7단계
    if len(id) == 1:
        id = id+(id[0]*2)
    if len(id) == 2:
        id = id+id[1]

    answer = id
    return answer