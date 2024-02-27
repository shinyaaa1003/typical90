import io
import sys

# input here
_INPUT = """\
5
e869120
atcoder
e869120
square1001
square1001

"""
sys.stdin = io.StringIO(_INPUT)

# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)

# 入力
N = int(input())
S = [input() for _ in range(N)]

names = set()
for i in range(N):
    if S[i] in names:
        continue
    names.add(S[i])
    print(i+1)
