import io
import sys

# input here
_INPUT = """\
4 3
1 2 314
1 3 159
1 4 265

"""
sys.stdin = io.StringIO(_INPUT)

# code 
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)
import heapq
def dijkstra(s):
    # グラフの入力はg[now] = [[cost, next], ...]の形で
    # 始点から各頂点への最短距離
    d = [float('inf')]*N
    d[s] = 0
    # 各頂点が訪問済みかどうか
    used = [False]*N
    used[s] = True
    # 仮の距離を記録するヒープ
    que = []
    for e in g[s]:
        heapq.heappush(que, e)
    while que:
        u, v = heapq.heappop(que)
        if used[v]:
            continue
        d[v] = u
        used[v] = True
        for e in g[v]:
            if not used[e[1]]:
                heapq.heappush(que, [e[0] + d[v], e[1]])
    return d

N,M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int, input().split())
    g[a-1].append([c,b-1])
    g[b-1].append([c,a-1])
    
d_start = dijkstra(0)
d_goal = dijkstra(N-1)
for i in range(N):
    print(d_start[i] + d_goal[i])