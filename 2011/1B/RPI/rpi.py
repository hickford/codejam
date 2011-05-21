#!python
# http://code.google.com/codejam/contest/dashboard?c=1150485#s=p0
from __future__ import division

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

def avg(X):
    return sum(X)/len(X)

def savg(X):
    Y = [x for x in X if x != None]
    return avg(Y)

def RPI(WP,OWP,OOWP):
    """RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP"""
    return 0.25 * WP + 0.50 * OWP + 0.25 * OOWP

for i in range(1,T+1):
    print "Case #%d:" % i
    S = list()
    N = int(f.readline())
    O = list()
    games = list()
    for j in range(N):
        X = [int(x) if x != '.' else None for x in f.readline().strip() ]
        S.append(X)
    #print S
    WPs = list()
    for j in range(N):
        WPs.append(savg(S[j]))
        O.append( [k for (k,y) in enumerate(S[j]) if y != None] )
        games.append(len(O[j]))
        assert j not in O[j]
    #print O
    #print WPs
    #pass
    OWPs = list()
    for j in range(N):
        WP = WPs[j]
        opponents = O[j]
        lowps = dict()
        for k in opponents:
            lowps[k] = (WPs[k]*games[k]-S[k][j])/(games[k]-1)
        OWP = avg(lowps.values())
        OWPs.append( OWP )
        
    for j in range(N):
        WP = WPs[j]
        opponents = O[j]
        OWP = OWPs[j]
        OOWP = avg([OWPs[k] for k in opponents])
        print RPI(WP,OWP,OOWP)
        pass
    #print "Case #%d: %s" % (i,clock)
