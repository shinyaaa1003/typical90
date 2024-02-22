import io
import sys

# input here
_INPUT = """\
10000000 3

"""
sys.stdin = io.StringIO(_INPUT)

# code 
def Eratosthenes(N):
    primes = [True] * (N+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(N**0.5)+1):
        if primes[i]:
            for j in range(i**2, N+1, i):
                primes[j] = False
    return primes

#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)
N,K = map(int, input().split())

num_prime_factors = [0] * (N+1)

for i in range(2,N+1):
    if num_prime_factors[i] != 0:
        continue
    for j in range(i ,N+1, i):
        num_prime_factors[j] += 1

ans = 0
for i in range(2,N+1):
    if num_prime_factors[i] >= K:
        ans += 1
print(ans)