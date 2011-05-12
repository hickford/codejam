#!python
# http://code.google.com/codejam/contest/dashboard?c=619102#
import sys
from optparse import OptionParser
from collections import deque
import itertools
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

def intersect((A1,B1),(A2,B2)):
    # do these wires intersect?
    # intersect iff sign(A1-A2) != sign(B1-B2)
    return cmp(A1-A2,0) != cmp(B1-B2,0)
    
T = int(f.readline())

for i in range(1,T+1):
    N = int(f.readline())
    wires = list()
    y = 0
    for j in range(N):
        wires.append( tuple(int(x) for x in f.readline().split() ) )
    for (A1,B1),(A2,B2) in itertools.combinations(wires,2):
        if intersect((A1,B1),(A2,B2)):
            y += 1
    print "Case #%d: %d" % (i,y)