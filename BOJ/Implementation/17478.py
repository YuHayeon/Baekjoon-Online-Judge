# 17478 : 재귀함수가 뭔가요?

import sys

input = sys.stdin.readline

n = int(input())

print_list = [
    '"재귀함수가 뭔가요?"',
    '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
    "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.",
    '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."',
    '"재귀함수는 자기 자신을 호출하는 함수라네"',
    "라고 답변하였지.",
]


def print_what_is_recursive_function(l):
    line = ""
    for _ in range(l):
        line += "____"

    if l == n:
        print(line + print_list[0])
        print(line + print_list[4])
        print(line + print_list[5])
        return

    for i in range(4):
        print(line + print_list[i])
    print_what_is_recursive_function(l + 1)

    print(line + print_list[5])


print(
    """어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
"재귀함수가 뭔가요?"
"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""""
)
if n > 0:
    print_what_is_recursive_function(1)
print("라고 답변하였지.")
