import io
import sys

# input here
_INPUT = """\
1 5
"""
sys.stdin = io.StringIO(_INPUT)

"""
#.#.#.#.#.
..........
#.#.#.#.#.
..........
#.#.#.#.#.
..........

"""
# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**9)

from math import ceil
# 入力
H, W = map(int, input().split())

if H == 1 or W == 1:
    print(H*W)
    exit()
print(ceil(H/2) * ceil(W/2))
