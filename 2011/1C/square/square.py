#!python
# http://code.google.com/codejam/contest/dashboard?c=1128486#s=p0
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

def solve(grid,R,C):
    for i in range(R):
        for j in range(C):
            x = grid[i][j]
            assert x in ('.','#')
            above = None
            left = None
            right = None
            below = None
            if j < C-1:
                right = grid[i][j+1]
            if i < R-1:
                below= grid[i+1][j] 
            if i > 0:
                above = grid[i-1][j]
            if j > 0:
                left = grid[i][j-1]
            if x == '.':
                if left and left=='c':
                    return False
                if above and above=='b':
                    return False
            elif x == '#':
                if (left not in ['a','c']) and above not in ['a','b']:
                    grid[i][j] = 'a'
                    if not right:
                        return False
                    if not below:
                        return False
                elif (left == 'a') and (above not in ['a','b']):
                    grid[i][j] = 'b'
                    if not below:
                        return False
                elif (above == 'a') and (left not in ['a','c']):
                    grid[i][j] = 'c'
                    if not right:
                        return False
                elif (above == 'b') and (left == 'c'):
                    grid[i][j] = 'd'
                else:
                    return False
    return grid
                    
        

for a in range(1,T+1):
    R, C = [int(x) for x in f.readline().split()]
    grid = list()
    for i in range(R):
        grid.append( list(f.readline().strip()) )
        
    #print grid
    print "Case #%d:" % a
    solution = solve(grid,R,C)
    if solution == False:
        answer = "Impossible"
        print answer
    else:
        for line in solution:
            x = "".join(line).replace("a","/").replace("b","\\").replace("c","\\").replace("d","/")
            print x
    
    
