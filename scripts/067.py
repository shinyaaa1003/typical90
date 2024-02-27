import io
import sys

# input here
_INPUT = """\
0 15
"""
sys.stdin = io.StringIO(_INPUT)

# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**9)


def base10tobaseN(target, N) -> str:
    '''N進数表記に変換, '''
    tmp = ''
    while target >= N:
        tmp = str(target % N) + tmp
        target //= N
    tmp = str(target) + tmp
    return tmp


def baseNtobase10(target: str, N) -> int:
    '''N進数を10進数に変換'''
    base10 = 0
    for i in range(1, len(target)+1):
        base10 += N**(i-1) * int(target[-i])
    return base10


# 入力
N, K = map(int, input().split())
for _ in range(K):
    N = baseNtobase10(str(N), 8)
    N = base10tobaseN(N, 9)
    N = N.replace("8", "5")
print(N)
