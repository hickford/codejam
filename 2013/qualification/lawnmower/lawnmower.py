#!python
"https://code.google.com/codejam/contest/2270488/dashboard#s=p1"

import fileinput, sys
import numpy
f = fileinput.input()
T = int(f.readline())

for case in range(1,T+1):
    N,M = [int(x) for x in f.readline().split()]
    heights = []
    for i in range(N):
        row = [int(x) for x in f.readline().split()]
        assert len(row) == M
        heights.append(row)
    
    # row, column
    heights = numpy.asarray(heights)
    
    column_maxes = numpy.amax(heights,axis=0)
    row_maxes = numpy.amax(heights,axis=1)
    
    possible = all(heights[i,j] in (row_maxes[i], column_maxes[j]) for i in range(N) for j in range(M))
    
    answer = "YES" if possible else "NO"
    print "Case #%d: %s" % (case, answer)
