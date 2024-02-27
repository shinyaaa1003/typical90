import io
import sys

# input here
_INPUT = """\
7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
10
1 3
2 4
3 5
4 6
5 7
1 5
2 6
3 7
1 6
2 7

"""
sys.stdin = io.StringIO(_INPUT)

# code
from itertools import accumulate
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**9)

N = int(input())
score_a = [0]*N
score_b = [0]*N


for _ in range(N):
    cla, score = map(int, input().split())
    if cla == 1:
        score_a[_] = score
    else:
        score_b[_] = score

acc_a = list(accumulate(score_a, initial=0))
acc_b = list(accumulate(score_b, initial=0))

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(acc_a[r]-acc_a[l-1], acc_b[r]-acc_b[l-1])
