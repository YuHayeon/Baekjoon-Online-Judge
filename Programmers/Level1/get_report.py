# https://programmers.co.kr/learn/courses/30/lessons/92334
# 프로그래머스 LEVEL 1 - 신고 결과 받기
# 2022 KAKAO BLIND RECRUITMENT

def solution(id_list, report, k):

    answer = []
    report_dic = {user: [] for user in id_list}
    report_cnt = {user: 0 for user in id_list}

    for s in report:
        reporter, user = s.split()
        if user not in report_dic[reporter]:
            report_dic[reporter].append(user)
            report_cnt[user] += 1

    for reporter in id_list:
        res = 0
        for user in report_dic[reporter]:
            if report_cnt[user] >= k:
                res += 1
        answer.append(res)

    return answer