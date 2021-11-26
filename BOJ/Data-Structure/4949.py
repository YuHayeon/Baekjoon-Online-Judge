# 4949 : 균형잡힌 세상

import sys

while (True):
    test = []

    string = sys.stdin.readline().rstrip()

    if string == '.':
        exit(0)

    for s in string:
        if s == '[':
            test.append('[')

        elif s == '(':
            test.append('(')

        elif s == ']':
            if test == [] or test[-1]=='(':
                result = "no"
                break
            else:
                test.pop()

        elif s == ')':
            if test == [] or test[-1]=='[':
                result = "no"
                break
            else:
                test.pop()

        if test == []:
            result = "yes"

    if test != []:
        result = "no"

    print(result)
