#!python
# http://code.google.com/codejam/contest/dashboard?c=975485#s=p3
import sys
from optparse import OptionParser
from collections import deque
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
    N = int(f.readline())
    array = [ int(x) for x in f.readline().split() ]
    array2 = sorted(array)
    answer = 0
    for a,b in zip(array,array2):
        answer += (not a==b)
    print "Case #%d: %s" % (i,answer)