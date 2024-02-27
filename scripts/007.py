import io
import sys

# input here
_INPUT = """\
10
869120000 998244353 777777777 123456789 100100100 464646464 987654321 252525252 869120001 1000000000
10
4229
20210406
1
268435456
3582
536870912
1000000000
869120
99999999
869120001


"""
sys.stdin = io.StringIO(_INPUT)

# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**9)


def binary_search(A, x):
    ok, ng = -1, len(A)
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if x >= A[mid]:
            ok = mid
        else:
            ng = mid
    return ok, ng


N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
for _ in range(Q):
    B = int(input())
    ok, ng = binary_search(A, B)
    if ok == -1:
        print(abs(A[0]-B))
    elif ng == N:
        print(abs(A[-1]-B))
    else:
        print(min(abs(A[ok]-B), abs(A[ng]-B)))
