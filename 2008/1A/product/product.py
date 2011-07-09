#!python
# http://code.google.com/codejam/contest/dashboard?c=32016#s=p0
import sys
from optparse import OptionParser
from collections import deque
import math
import operator
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
    
def vproduct(X,Y):
    return sum(x*y for (x,y) in zip(X,Y))
    
T = int(f.readline())

# if a < b and x < y then ay+bx<ax+by

for i in range(1,T+1):
    n = int(f.readline())
    X = [int(x) for x in f.readline().split()]
    Y = [int(x) for x in f.readline().split()]
    z = vproduct(sorted(X),reversed(sorted(Y)))
    print "Case #%d: %d" % (i,z)