#!python
# http://code.google.com/codejam/contest/dashboard?c=619102#s=p1
from __future__ import division
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

for i in range(1,T+1):
    L,P,C = ( int(x) for x in f.readline().split() )
    s = math.ceil(math.log(P/L,C))       # how many powers of C apart?
    X = math.ceil(math.log(s,2))         # binary search among these powers
    print "Case #%d: %d" % (i,X)