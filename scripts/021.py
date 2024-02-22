import io
import sys

# input here
_INPUT = """\
4 7
1 2
2 1
2 3
4 3
4 1
1 4
2 3

"""
sys.stdin = io.StringIO(_INPUT)

# code 
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)
from atcoder.scc import SCCGraph
N,M = map(int, input().split())
g = SCCGraph(N)
for _ in range(M):
    a,b = map(int, input().split())
    g.add_edge(a-1, b-1)

groups = g.scc()

ans = 0
for group in groups:
    ans += len(group) * (len(group) - 1) // 2   
    
print(ans)