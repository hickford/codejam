#!python
# Cheating a Boolean Tree http://code.google.com/codejam/contest/dashboard?c=32001#s=p0
import sys
from optparse import OptionParser
import operator
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
    
def left(n):
    """Is node n a left descendant of the root in a zero-indexed boolean tree?"""
    while n > 2:
        n = (n-1)//2
    return n == 1
    
class BooleanTree:
    def __init__(self,nodeinfo,debug=False,adamsize=None):
        self.leaf = (len(nodeinfo) == 1)
        if self.leaf:
            self.value = nodeinfo[0]
        self.adamsize = adamsize if adamsize else len(nodeinfo)
        self.solutions = dict()
        if debug:
            print nodeinfo
        if not self.leaf:
            self.gate,self.changeable = nodeinfo[0]
            self.left = BooleanTree([x for (i,x) in enumerate(nodeinfo) if left(i)],adamsize=self.adamsize)
            self.right = BooleanTree([x for (i,x) in enumerate(nodeinfo) if i>0 and not left(i)],adamsize=self.adamsize)
        
    def ma(self,V):
        """What is the minimum number of gates that can be changed to make the root of this boolean tree evaluate to V? Return a number greater than the number of nodes M if not possible."""
        try:
            return self.solutions[V]
        except KeyError:
            pass
            
        if self.leaf:
            self.solutions[V] = 0 if self.value == V else self.adamsize+1
            return self.solutions[V]
            
        possibles = [self.adamsize+1]
        for logic in (operator.or_, operator.and_):
            for i in (0,1):
                for j in (0,1):
                    if logic(i,j)==V:
                        if self.gate == logic:
                            penalty = 0
                        elif self.changeable:
                            penalty = 1
                        else:
                            # penalty = self.adamsize+1
                            continue
                        l = self.left.ma(i)
                        r = self.right.ma(j)
                        possibles.append(penalty+l+r)
                        
        self.solutions[V] = min(possibles)
        return self.solutions[V]
        
        
        
T = int(f.readline())
                      
for i in range(1,T+1):
    M, V = [int(x) for x in f.readline().split()]
    assert M % 2 == 1
    assert V in (0,1)
    nodeinfo = list()
    #The first (M-1)/2 lines describe the interior nodes. Each line contains G and C, each being either 0 or 1. If G is 1 then the gate for this node is an AND gate, otherwise it is an OR gate. If C is 1 then the gate for this node is changeable, otherwise it is not. Interior node X has nodes 2X and 2X+1 as children.
    for j in range( (M-1)//2 ):
        G, C = [int(x) for x in f.readline().split()]
        C = bool(C)
        G = operator.and_ if G == 1 else operator.or_
        nodeinfo.append((G,C))
    #The next (M+1)/2 lines describe the leaf nodes. Each line contains one value I, 0 or 1, the value of the leaf node.
    for j in range( (M+1)//2 ):
        I = int(f.readline())
        nodeinfo.append(I)
    T = BooleanTree(nodeinfo,debug=False)
    x = T.ma(V)
    answer = "IMPOSSIBLE" if x > M else x
    print "Case #%d: %s" % (i,answer)
