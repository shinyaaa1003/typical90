import io
import sys

# input here
_INPUT = """\
10 1 0
0 0 0 0 0 0 0 0 0 0

"""
sys.stdin = io.StringIO(_INPUT)

# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)

from itertools import combinations
# 入力
N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for a, b, c, d, e in combinations(A, 5):
    if a % P * b % P * c % P * d % P * e % P % P == Q:
        ans += 1

print(ans)
