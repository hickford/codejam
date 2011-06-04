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

upper_bound = 10**12
# we only need to compute primepi up to sqrt of this

import cPickle as pickle
g = open("primes.dump") # primes up to 10**6
primes = pickle.load(g)
g.close()

import bisect

def primepi(x):
    """Return the number of primes less than or equal to N"""
    return bisect.bisect(primes,x)

assert primepi(1) == 0
assert primepi(2) == 1
assert primepi(100) == 25

for i in range(1,T+1):
    N = int(f.readline())
    answer = 0
    if N == 1:
        answer = 0
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

    print "Case #%d: %s" % (i,answer)

