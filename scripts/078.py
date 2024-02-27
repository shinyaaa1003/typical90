import io
import sys

# input here
_INPUT = """\
7 18
7 2
1 6
5 2
1 3
7 6
5 3
5 6
5 4
1 7
2 6
3 4
5 1
4 7
4 6
5 7
3 2
4 2
1 4

"""
sys.stdin = io.StringIO(_INPUT)

# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)

# 入力
N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

ans = 0
for i in range(N):
    adj_num = 0
    for adj in g[i]:
        if adj < i:
            adj_num += 1
    if adj_num == 1:
        ans += 1
print(ans)
