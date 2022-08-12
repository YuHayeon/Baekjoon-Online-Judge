# 2493 : 탑

import sys
input = sys.stdin.readline


def stack(n, top_list, result):
    top_index = [i for i in range(n)]
    stack = []
    stack.append(top_index.pop())

    while top_index:
        if stack and top_index and top_list[top_index[-1]] > top_list[stack[-1]]:
            result[stack[-1]] = len(top_index)
            stack.pop()

        else:
            stack.append(top_index.pop())

    return result


if __name__ == "__main__":
    n = int(input())
    top_list = list(map(int, input().split()))
    result = [0 for _ in range(n)]

    print(*stack(n, top_list, result))
