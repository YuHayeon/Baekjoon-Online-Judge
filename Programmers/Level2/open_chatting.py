# https://programmers.co.kr/learn/courses/30/lessons/42888
# 프로그래머스 LEVEL 1 - 오픈 채팅방
# 2019 KAKAO BLIND RECRUITMENT

def solution(record):
    user = {}
    log = []
    answer = []

    for s in record:
        if s[0] == 'L':
            state, uid = s.split()
        else:
            state, uid, nickname = s.split()
            user[uid] = nickname
        log.append((state, uid))

    for state, uid in log:
        if state == "Enter":
            answer.append(str(user.get(uid)) + "님이 들어왔습니다.")
        elif state == "Leave":
            answer.append(str(user.get(uid)) + "님이 나갔습니다.")

    return answer