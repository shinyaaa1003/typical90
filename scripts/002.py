import io
import sys

# input here
_INPUT = """\
3

"""
sys.stdin = io.StringIO(_INPUT)

# code 
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)
"""
00 (( 
01 ()
10 )(
11 ))
"""

def isok(S):
    c = 0
    for s in S:
        if s == '(':
            c += 1
        else:
            c -= 1
        if c < 0:
            return False
    if c == 0:
        return True
    else:
        return False

def main():
    N = int(input())
    
    for i in range(2**N):
        tmp = ''
        for j in range(N-1, -1, -1):
            if (i>>j)&1 == 1:
                tmp += ')'
            else:
                tmp += '('
        if isok(tmp):
            print(tmp)


if __name__ == "__main__":
    main()