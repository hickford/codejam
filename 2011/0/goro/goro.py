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

for i in range(1,T+1):
    N = int(f.readline())
    array = [ int(x) for x in f.readline().split() ]
    array2 = sorted(array)
    answer = 0
    for a,b in zip(array,array2):
        answer += (not a==b)
    print "Case #%d: %s" % (i,answer)