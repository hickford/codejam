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
           
import sieve
import math
import gcd
from mpmath import primepi

       
def root(N,k):
    """return integer part of kth root of N"""
    # SAFELY
    x0 = int(N**(1/k))
    if (x0+1)**k <= N:
        return x0+1
    elif x0**k <= N:
        return x0
    elif (x0-1)**k <= N:
        return x0-1
    raise Exception

for i in range(1,T+1):
    N = int(f.readline())
    answer = 0
    if N == 1:
        answer = 0
    else:
        answer = 1
        k = 2
        #x = int(N**(1/k))        # this was why I went wrong at N=125
        x = root(N,k)
        while x >= 2:
            answer += primepi(x)
            k += 1
            x = root(N,k)


    # slow. agrees up to 125
    """primes = sieve.sieve(N)
    most = 1 + sum([int(math.floor(math.log(N,p))) for p in primes])
    # p is counted for each k p**k is less than N
    # so take pi(N) + pi(N**1/2) + pi(N**1/3) and so on
    guess = max(len(primes),1)
    #print answer,most-guess

    print N, answer, most-guess
    assert answer==most-guess"""

    print "Case #%d: %s" % (i,answer)
        
        
