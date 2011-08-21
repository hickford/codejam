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
    def __init__(self,nodeinfo,debug=False):
        self.M = len(nodeinfo)
        self.leaf = (self.M == 1)
        if self.leaf:
            self.value = nodeinfo[0]
        self.solutions = dict()
        if debug:
            self.nodeinfo = nodeinfo
            print nodeinfo
        if not self.leaf:
            self.gate,self.changeable = nodeinfo[0]
            leftinfo = list()
            rightinfo = list()
            for (i,x) in enumerate(nodeinfo):
                if i == 0:
                    continue
                if left(i):
                    leftinfo.append(x)
                else:
                    rightinfo.append(x)
            self.left = BooleanTree(leftinfo)
            self.right = BooleanTree(rightinfo)
        
    def ma(self,V):
        try:
            return self.solutions[V]
        except KeyError:
            pass
        if self.leaf:
            self.solutions[V] = 0 if self.value == V else False
            return self.solutions[V]
        possibles = list()
        if V == 0:
            if self.gate == "or" or self.changeable:
                penalty = 1 if (self.changeable and self.gate != "or") else 0
                # 0 = 0 or 0 only
                l = self.left.ma(0)
                r = self.right.ma(0)
                if l is not False and r is not False:
                    possibles.append( penalty + l + r)
            if self.gate == "and" or self.changeable:
                penalty = 1 if (self.changeable and self.gate != "and") else 0
                # 0 = 0 and 1
                l = self.left.ma(0)
                r = self.right.ma(1)
                if l is not False and r is not False:
                    possibles.append( penalty + l + r)            
                # 0 = 1 and 0
                l = self.left.ma(1)
                r = self.right.ma(0)
                if l is not False and r is not False:
                    possibles.append( penalty + l + r)            
                # 0 = 0 and 0
                l = self.left.ma(0)
                r = self.right.ma(0)
                if l is not False and r is not False:
                    possibles.append( penalty + l + r)                   
        elif V==1:
            if self.gate == "or" or self.changeable:
                penalty = 1 if (self.changeable and self.gate != "or") else 0
                # 1 = 0 or 1
                l = self.left.ma(0)
                r = self.right.ma(1)
                if l is not False and r is not False:
                    possibles.append( penalty + l + r)            
                # 1 = 1 or 0
                l = self.left.ma(1)
                r = self.right.ma(0)
                if l is not False and r is not False:
                    possibles.append( penalty + l + r)            
                # 1 = 1 or 1
                l = self.left.ma(1)
                r = self.right.ma(1)
                if l is not False and r is not False:
                    possibles.append( penalty + l + r)                   
            if self.gate == "and" or self.changeable:
                penalty = 1 if (self.changeable and self.gate != "and") else 0
                # 1 = 1 and 1 only
                l = self.left.ma(1)
                r = self.right.ma(1)
                if l is not False and r is not False:
                    possibles.append( penalty + l + r)
        
        self.solutions[V] = min(possibles) if possibles else self.M+1
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
        G = "and" G == 1 else "or"
        nodeinfo.append((G,C))
    #The next (M+1)/2 lines describe the leaf nodes. Each line contains one value I, 0 or 1, the value of the leaf node.
    for j in range( (M+1)//2 ):
        I = int(f.readline())
        nodeinfo.append(I)
    
    T = BooleanTree(nodeinfo,debug=False)
    x = T.ma(V)
    answer = "IMPOSSIBLE" if x is False else x
    print "Case #%d: %s" % (i,answer)