#!python
from optparse import OptionParser
from collections import deque
usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if not args:
	parser.error("input omitted")
if args[0] == "-":
    import sys
    f = sys.stdin
else:
    f = open(args[0])
T = int(f.readline())

def psum(x,y):
    return x^y

for i in range(1,T+1):
    N = int(f.readline())
    candies = [ int(x) for x in f.readline().split()  ]
    if reduce(psum,candies) == 0:
        answer = sum(candies) - min(candies)
    else:
        answer = "NO"
    print "Case #%d: %s" % (i,answer)