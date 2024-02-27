import io
import sys

# input here
_INPUT = """\
6
1 1000000000
2 200000000
1 30000000
2 4000000
1 500000
3 3


"""
sys.stdin = io.StringIO(_INPUT)

# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)

from collections import deque
# 入力
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

deq = deque()

for i in range(Q):
    ope, x = query[i]
    if ope == 1:
        deq.appendleft(x)
    elif ope == 2:
        deq.append(x)
    else:
        print(deq[x-1])
