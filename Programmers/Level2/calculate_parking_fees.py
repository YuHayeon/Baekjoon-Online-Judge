# https://school.programmers.co.kr/learn/courses/30/lessons/92341
# Programmers LEVEL 2 - 주차 요금 계산
# 2022 KAKAO BLIND RECRUITMENT


def parsing_car_number(records):
    records_dict = {}

    for record in records:
        time, car, status = record.split(" ")

        if car in records_dict:
            records_dict[car].append(time)
        else:
            records_dict[car] = [time]

    records_dict = dict(sorted(records_dict.items()))
    return records_dict


def parsing_time(start, end):
    start_hour, start_min = map(int, start.split(":"))
    end_hour, end_min = map(int, end.split(":"))

    hour = end_hour - start_hour
    min = end_min - start_min
    if start_min > end_min:
        hour -= 1
        min += 60

    time = (hour*60)+min

    return time


def calculating_fees(fees, time):
    default_time, default_fees, unit_time, unit_fees = fees[0], fees[1], fees[2], fees[3]
    result_fees = 0

    if time <= default_time:
        result_fees = default_fees
    else:
        result_fees = default_fees
        if (time-default_time) % unit_time > 0:
            result_fees += (((time-default_time) // unit_time) + 1) * unit_fees
        else:
            result_fees += ((time-default_time) // unit_time) * unit_fees
    return result_fees


def solution(fees, records):
    records_dic = parsing_car_number(records)
    answer = []

    for car in records_dic:
        record = records_dic[car]
        if len(record) % 2 == 1:
            record.append("23:59")

        time = 0
        for i in range(0, len(record), 2):
            time += parsing_time(record[i], record[i+1])

        answer.append(calculating_fees(fees, time))

    return answer


fees = [180, 5000, 10, 600]

records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))
