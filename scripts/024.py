import io
import sys

# input here
_INPUT = """\
7 999999999
3 1 4 1 5 9 2
1 2 3 4 5 6 7

"""
sys.stdin = io.StringIO(_INPUT)

# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)

# 入力
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = 0
for i in range(N):
    diff += abs(A[i] - B[i])

if diff <= K and (K - diff) % 2 == 0:
    print('Yes')
else:
    print('No')
