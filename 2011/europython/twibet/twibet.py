#!python
# http://code.google.com/codejam/contest/dashboard?c=1277486#s=p3
import sys
from optparse import OptionParser
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
from pygraph.classes.digraph import digraph
from pygraph.algorithms.accessibility import accessibility
for i in range(1,T+1):
    N = int(f.readline())
    fols = [int(x) for x in f.readline().split()]
    assert len(fols) == N
    G = digraph()
    for a in range(1,N+1):
        G.add_node(a)
    for j,a in enumerate(G.nodes()):
        assert a != fols[j]
        G.add_edge((fols[j],a))     # edge (b,a) means b follows a
    print "Case #%d:" % i
    A = accessibility(G)
    #print A
    for a in range(1,N+1):
        print len(A[a])