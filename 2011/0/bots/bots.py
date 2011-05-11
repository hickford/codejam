#!python
# http://code.google.com/codejam/contest/dashboard?c=975485#
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
    freesince = dict(O=0,B=0)
    position = dict(O=1,B=1)
    line = deque(f.readline().split())
    N = int(line.popleft())
    
    clock = 0
    
    while line:
        bot, target = line.popleft(), int(line.popleft())
        d = abs(target-position[bot])
        
        # move
        clock += max(0, d - (clock - freesince[bot]) )
        position[bot] = target

        # push button
        clock += 1
        freesince[bot] = clock
        
    print "Case #%d: %s" % (i,clock)
