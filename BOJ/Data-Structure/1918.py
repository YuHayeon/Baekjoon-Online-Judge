# 1918 : 후위 표기식
import sys

string = sys.stdin.readline().strip()
op = []
result = ''

for s in string:
    if s.isalpha():
        result += s
    else:
        if s == '(':
            op.append(s)

        elif s == ')':
            while op and op[-1] != '(':
                result += op.pop()
            op.pop()

        elif s == '*' or s == '/':
            while op and (op[-1] == '*' or op[-1] == '/'):
                result += op.pop()
            op.append(s)

        elif s == '+' or s == '-':
            while op and op[-1] != '(':
                result += op.pop()
            else:
                op.append(s)

while op:
    result += op.pop()

print(result)
