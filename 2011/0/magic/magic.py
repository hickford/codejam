#!python
from collections import deque
from optparse import OptionParser
usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if not args:
	parser.error("input omitted")
if args[0] == "-":
    import sys
    f = sys.stdin
else:
    f = open(args[0])
T = int(f.readline())

for i in range(1,T+1):
    combinations = dict()
    oppositions = list()
    elist = ""
    
    line = deque(f.readline().split())
    C = int(line.popleft())
    for j in range(C):
        abc = line.popleft()
        assert len(abc) == 3
        a,b,c = abc
        combinations[a+b] = c
        combinations[b+a] = c        
    D = int(line.popleft())
    for j in range(D):
        ab = line.popleft()
        assert len(ab)==2
        oppositions.append(frozenset(ab))
    N = int(line.popleft())
    series = line.popleft()
    assert len(series)==N
    assert not line
    #print combinations,oppositions,series
    for x in series:
        elist += x
        
        # check for combinations
        end = elist[-2:]
        if combinations.has_key(end):
            elist = elist[:-2] + combinations[end]
            
        # check for opposition
        eset = set(elist)
        for pair in oppositions:
            if pair <= eset:    # containment
                elist = ""
                break

        #print x, elist
                
                
    
    answer = "[" + ", ".join(elist) + "]"
    
    print "Case #%d: %s" % (i,answer)
