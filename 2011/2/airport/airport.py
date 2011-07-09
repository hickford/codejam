#!python
# Airport Walkways http://code.google.com/codejam/contest/dashboard?c=1150486#s=p0
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
                      
for i in range(1,T+1):
    X,S,R,t,N = [int(x) for x in f.readline().split()]
    assert S <= R
    
    pos = 0
    
    belts = defaultdict(int)
    # distance at each walkway speed, counting absence of walkway as speed 0
    
    for j in range(N):
        B,E,w = [int(x) for x in f.readline().split()]
        assert B >= pos
        belts[0] += B-pos
        pos = B
        assert E > B
        belts[w] += E-B
        pos = E
    # finally
    assert pos == E
    assert X >= pos
    belts[0] += X - E
    pos = X
    assert sum(belts.values()) == X
    celts = OrderedDict(sorted(belts.items(), key=lambda t: t[0]))
    
    clock = 0
    sprintwatch = t
  
    for w,d in celts.items():
        assert sprintwatch >= 0
        v0 = w + S  # walkway + walking
        v1 = w + R  # walkway + run
        if sprintwatch == 0:
            # we must walk
            clock += d / v0
        else:
            # sprint as much as we can
            if v1 * sprintwatch >= d:
                # we can sprint all of it
                t1 = d / v1
                sprintwatch -= t1
                clock += t1
            else:
                # sprint the start
                d1 = v1 * sprintwatch
                #t1 = d1/v1
				t1 = sprintwatch
                sprintwatch -= t1
                assert sprintwatch == 0
                clock += t1
                # walk the rest
                d0 = d - d1
                assert d0 > 0
                t0 = d0/v0
                clock += t0
            
    print "Case #%d: %s" % (i,clock)
        
        