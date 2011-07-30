#!python
# Welcome to Codejam http://code.google.com/codejam/contest/dashboard?c=90101#s=p2
import math
import sys
from collections import defaultdict
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

def count(text,phrase):
    """Return number of times that phrase occurs as a subsequence of text"""
    if not phrase:
        raise ValueError
    text = [x for x in text if x in phrase]
    
    n = len(text)
    m = len(phrase)
    
    positions = defaultdict(list)
    for i,x in enumerate(positions):
        positions[x].append(i)
    
    """ P[j][i] is number of times the first j+1 letters of phrase occur as a subsequence in text ending at position i"""
    P = [list() for j in range(len(phrase))]
    
    x = phrase[0]
    P[0] = [int(y==x) for y in text]
    
    for j in range(1,len(phrase)):
        cumulator = 0
        x = phrase[j]
        for i,y in enumerate(text):
            cumulator += P[j-1][i]
            if y==x:
                #P[j][i] = cumulator
                P[j].append(cumulator)
            else:
                #P[j][i] == 0
                P[j].append(0)
        
    
    return sum(P[j][i] for i in range(len(text)))


magic_words = "welcome to code jam"

for i in range(1,T+1):
    line = f.readline().rstrip("\n")
    answer = count(line,magic_words)
    print "Case #%d: %.4d" % (i,answer % 10**4)
