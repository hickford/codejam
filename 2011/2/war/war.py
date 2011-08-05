#!python
# AI War http://code.google.com/codejam/contest/dashboard?c=1150486#s=p3
"""This is me implementing the problem author's solution from  http://code.google.com/codejam/contest/dashboard?c=1150486#s=a&a=3"""
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
    
from pygraph.classes.graph import graph    
from pygraph.algorithms.minmax import shortest_path  
from collections import defaultdict
T = int(f.readline())
for i in range(1,T+1):
    P,W = [int(x) for x in f.readline().split()]
    G = graph()
    for x in range(P):
        G.add_node(x)
    wormholes = [tuple(int(x) for x in s.split(",")) for s in f.readline().split()]
    for (x,y) in wormholes:
        G.add_edge((x,y))
    # our home planet is 0
    # AI's home planet is 1
    tree, distance = shortest_path(G,0) # distance of each vertex from 0
    D = distance[1]
    vertices_by_distance = defaultdict(list)
    for v,d in distance.items():
        vertices_by_distance[d].append(v)
    
    def H(a,b,c):
        """Number of neighbors of c that are not neighbors of either a or b."""
        return len( set(G.neighbors(c)) - set(G.neighbors(a)) - set(G.neighbors(b)) )
        
    F = dict()  # Let F(a, b) := the maximum number of planets threatened or conquered by a shortest path 0-...-a-b , defined for adjacent vertices a and b such that distance[b]==distance[a]+1
    
    Pre = dict()
    for a in vertices_by_distance[1]:
        F[(0,a)] = len(set([0,a]+G.neighbors(0)+G.neighbors(a)))
    
    for d in range(1,D-1):
        for b in vertices_by_distance[d]:
            for c in G.neighbors(b):
                if distance[c]==d+1:
                    F[(b,c)] = max( F[(a,b)] + H(a,b,c) for a in G.neighbors(b) if distance[a] == d-1 )

                    # where did you come from?
                    for a in G.neighbors(b):
                        if distance[a]==d-1:
                            if F[(a,b)] + H(a,b,c) == F[(b,c)]:
                                Pre[(b,c)]=a
                    
    # F(b, c) = max_a { F(a, b) + G(a, b, c) }  

    #from pygraph.readwrite import dot
    #print dot.write(G)
    
    ### The answer to the problem is the maximum value of F(b, c) - D, where b, c are adjacent, dist[b] = D-2, dist[c] = D-1, and c is adjacent to 1.
    t = None
    if D==1:
        t = len(set(G.neighbors(0)))
    elif D>1:
        for c in G.neighbors(1):
            if distance[c]==D-1:
                for b in G.neighbors(c):
                    if distance[b] == D-2:
                        x = F[(b,c)]-D
                        if x>t or t==None:
                            bmax = b
                            cmax = c
                            t = x
        path = [cmax,bmax]
        while path[-1] != 0:
            path.append(Pre[(path[-1],path[-2])])
        #print path
    print "Case #%d: %d %d" % (i,D-1,t)
