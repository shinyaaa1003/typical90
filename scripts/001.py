import io
import sys

# input here
_INPUT = """\
3 100
2
28 54 81

"""
sys.stdin = io.StringIO(_INPUT)

# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**9)


def isok(A, K, L, mid):
    cnt = 0
    pre = 0
    for a in A:
        if a - pre >= mid:
            cnt += 1
            pre = a
    if L - pre >= mid:
        cnt += 1
    return cnt > K


def main():
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))

    ok, ng = 0, L+1
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if isok(A, K, L, mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()
