import io
import sys

# input here
_INPUT = """\
100 4
27 100
8 39
83 97
24 75

"""
sys.stdin = io.StringIO(_INPUT)

# code 
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)
W,N = map(int, input().split())
from atcoder.lazysegtree import LazySegTree
INF = 1 << 63
ID = INF


def op(ele1, ele2):
    return max(ele1, ele2)


def mapping(func, ele):
    if func == ID:
        return ele
    else:
        return func


def composition(func_upper, func_lower):
    if func_upper == ID:
        return func_lower
    else:
        return func_upper


e = -INF
id_ = ID

# TODO (初期リストlst)
lst = [0] * W
seg = LazySegTree(op, e, mapping, composition, id_, lst)
for _ in range(N):
    L,R = map(int, input().split())
    L -= 1
    max_h = seg.prod(L, R)
    seg.apply(L, R, max_h+1)
    print(max_h+1)