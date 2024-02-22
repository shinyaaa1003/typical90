import io
import sys

# input here
_INPUT = """\
31
1 2
1 3
2 4
2 5
3 6
3 7
4 8
4 9
5 10
5 11
6 12
6 13
7 14
7 15
8 16
8 17
9 18
9 19
10 20
10 21
11 22
11 23
12 24
12 25
13 26
13 27
14 28
14 29
15 30
15 31

"""
sys.stdin = io.StringIO(_INPUT)

# code 
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)
N = int(input())
g = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    
def dfs(now):
    for nex in g[now]:
        if dist[nex] != -1:
            continue
        dist[nex] = dist[now] + 1
        dfs(nex)
        
dist = [-1] * N
dist[0] = 0
dfs(0)
max_dist_idx = dist.index(max(dist))

dist = [-1] * N
dist[max_dist_idx] = 0
dfs(max_dist_idx)
print(max(dist) + 1)