import io
import sys

# input here
_INPUT = """\
4 4
3 1 4 1
5 9 2 6
5 3 5 8
9 7 9 3

"""
sys.stdin = io.StringIO(_INPUT)

# code 
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)
H,W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

row_sum = [0] * H
col_sum = [0] * W
for i in range(H):
    for j in range(W):
        row_sum[i] += A[i][j]
        col_sum[j] += A[i][j]

ans = [[None] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        ans[i][j] = row_sum[i] + col_sum[j] - A[i][j]

for a in ans:
    print(*a)