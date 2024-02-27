import io
import sys

# input here
_INPUT = """\
1000000000000000000 999999999999999999 999999999999999998

"""
sys.stdin = io.StringIO(_INPUT)

# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**9)
A, B, C = map(int, input().split())


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


cubic_size = gcd(gcd(A, B), C)
print(A//cubic_size + B//cubic_size + C//cubic_size - 3)
