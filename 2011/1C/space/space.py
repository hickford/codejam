#!python
# http://code.google.com/codejam/contest/dashboard?c=1128486#s=p1
from __future__ import division

import sys
from optparse import OptionParser
from collections import deque, defaultdict
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
    line = [int(x) for x in f.readline().split()]
    L, t, N, C = line[:4]
    preA = line[4:]
    A = deque()
    while len(A) < N:
        A.extend(preA[:])
    while len(A) > N:
        A.pop()
    
    time = 0
    position = 0
    # how far when boosters come online
    pos_online = 0.5 * t
    
    while A and time + A[0]/0.5 <= t :        # booster
        x = A.popleft()
        time += x/0.5
        position += x
    
    if A:
        # first bit of next journey without booster
        assert time <= t
        t0 = (t-time)
        
        time += t0
        A[0] -= t0*0.5      # do this bit without booster
        assert A[0] > 0
        
        remaining = sorted(A,reverse=True)
        boosted = remaining[:L]
        without = remaining[L:]
        
        time += sum(boosted)
        time += sum(without)/0.5
        
    print "Case #%d: %d"% (i,time)