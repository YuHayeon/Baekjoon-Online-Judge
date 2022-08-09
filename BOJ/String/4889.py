# 4889 : 안정적인 문자열

import sys
input = sys.stdin.readline


def stack(bracket_list):
    left_bracket = []
    right_bracket = []

    while bracket_list:
        last_bracket = bracket_list.pop()

        if last_bracket == "}":
            right_bracket.append(last_bracket)
        elif last_bracket == "{":
            if right_bracket:
                right_bracket.pop()
            else:
                left_bracket.append(last_bracket)

    return len(left_bracket), len(right_bracket)


def count_unstable(left_count, right_count):
    result = 0
    if left_count % 2 == 1:
        result += 1
    if right_count % 2 == 1:
        result += 1
    left_count = left_count // 2
    right_count = right_count // 2

    result += left_count+right_count
    return result


if __name__ == "__main__":
    i = 1
    while True:
        bracket_list = list(map(str, input().strip()))
        if "-" in bracket_list:
            break
        left_count, right_count = stack(bracket_list)
        result = count_unstable(left_count, right_count)
        print(f"{i}. {result}")
        i += 1
