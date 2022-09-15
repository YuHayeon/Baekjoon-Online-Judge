# 1049 : 기타줄

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
package_list = []
one_list = []
for _ in range(m):
    package, one = map(int, input().split())
    package_list.append(package)
    one_list.append(one)

package_min = min(package_list)
one_min = min(one_list)

quotient = n // 6
remainder = n % 6

result = min((package_min*(quotient+1)), one_min*n)
result = min(result, (package_min*quotient+one_min*remainder))

print(result)
