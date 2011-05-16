#!python
# http://code.google.com/codejam/contest/dashboard?c=189252#s=p0
import sys
from optparse import OptionParser
from collections import deque
import math
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

def mex(S):
    """return minimal r not in S (in natural numbers)"""
    r = 0
    while r in S:
        r += 1
    return r

for i in range(1,T+1):
    X = f.readline().strip()
    translation = dict()
    translation[X[0]] = 1   # first numeral is 1
    base = max(2, len(set(X)) )
    V = 0
    L = len(X)
    for (n,x) in enumerate(X):
        try:
            y = translation[x]
        except KeyError:
            y = mex(translation.values())
            translation[x] = y
        V += y * base**(L-n-1)
    print "Case #%d: %d" % (i,V)