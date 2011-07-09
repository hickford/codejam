#!python
# http://code.google.com/codejam/contest/dashboard?c=1150486#s=p2
from __future__ import division
import math
import sys
from optparse import OptionParser
from collections import deque, defaultdict, OrderedDict
usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if args:
    if args[0] == "-":
        f = sys.stdin
    else:
        f = open(args[0])
elif not sys.stdin.isatty():
    f = sys.stdin
else:
    parser.error("Need input from file or stdin")

T = int(f.readline())
                 
def nth_root(N,k):
    """Return greatest integer x such that x**k <= N"""
    x = int(N**(1/k))      
    while (x+1)**k <= N:
        x += 1
    while x**k > N:
        x -= 1
    assert x**k <= N < (x+1)**k    
    return x

upper_bound = math.sqrt(10**12)
# we only need to compute primepi up to sqrt of this

import cPickle as pickle
try:
    g = open("primes.dump")
    primes = pickle.load(g)
    g.close()
except:
    def sieve(n = None, primelist = [2]):
        """Iterator. Yield primes [less than or equal to n]"""
        for p in primelist:
            if n and p > n:
                raise StopIteration
            yield p

        x = primelist[-1]+1
        
        while not n or x <= n:
            limit = int(math.sqrt(x))
            for p in primelist:
                if p > limit:
                    # x is prime
                    primelist.append(x)
                    yield x
                    break
                if x % p == 0:
                    # x is composite
                    break
            x += 1
    primes = list(sieve(upper_bound))
    g = open("primes.dump",'wb')
    pickle.dump(primes,g,-1)
    g.close()

import bisect

def primepi(x):
    """Return the number of primes less than or equal to N"""
    return bisect.bisect(primes,x)

assert primepi(1) == 0
assert primepi(2) == 1
assert primepi(100) == 25

def spread(N):
    if N == 1:
        return 0
    else:
        # most waiters = sum(greatest k such that p**k <= N over p a prime less than or equal to N)
        #              = pi(n) + pi(n**1/2) + pi(n**1/3) + pi(n**1/4) + ..              # by counting
        # fewest waiters = pi(n)
        answer = 1
        k = 2
        x = nth_root(N,k)
        while x >= 2:
            answer += primepi(x)
            k += 1
            x = nth_root(N,k)
        return answer

def ilog(N,p):
    """Return greatest integer exponent x such that p**x <= N"""
    x = int(math.log(N,p))
    while p**(x+1) <= N:
        x += 1
    while p**x > N:
        x -= 1
    assert p**x <= N < p**(x+1)    
    return x
        
def spread2(N):
    """slow"""
    P = primes[:bisect.bisect(primes,N)]
    most = 1+sum([ilog(N,p) for p in P])
    least = max(1,primepi(N))
    return most-least
   
for i in range(1,T+1):
    N = int(f.readline())
    answer = spread(N)
    print "Case #%d: %s" % (i,answer)

