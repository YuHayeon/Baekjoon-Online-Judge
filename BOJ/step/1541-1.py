# 1541 : 잃어버린 괄호

import sys
import re

string = sys.stdin.readline().rstrip()
s_num = re.split(r'[-,+]', string)
result = ['(', str(int(s_num[0]))]

i=1
for s in string:
    if s == '+' :
        result.append('+',)
        result.append(str(int(s_num[i])))
        i += 1
    elif s == '-':
        result.append(')-(')
        result.append(str(int(s_num[i])))
        i += 1

result.append(')')
result = "".join(result)
print(eval(result))
