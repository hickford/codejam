#!python
# Millionaire http://code.google.com/codejam/contest/32005/dashboard#s=p2
from __future__ import division
import fileinput
import math
f = fileinput.input()
T = int(f.readline())

def solve(p,m):
    # too slow for large case :/
    game = dict()
    game[0] = [0,1] 
    for n in range(1,m+1):
        game[n]=[0]*(2**n) + [1]
        for fortune in range(0,2**n):
            for stake in range(0,fortune+1):
                
                #print "round %d fortune %d stake %d" % (n, fortune,stake)
                
                win_case = min(fortune+stake,2**n)
                lose_case = (fortune-stake)
                
                              
                expectation = p*game[n-1][win_case//2] + (1-p)*game[n-1][lose_case//2]
                
                if expectation > game[n][fortune]:
                    game[n][fortune] = expectation
                
                # stake j
            #print
        #print
    
    return game
    
i=1
for line in f:
    row = line.split()
    m = int(row[0])
    p = float(row[1])
    x = int(row[2])
    
    game=solve(p,m)
    
    fortune = min(2**m, x*2**m // 10**6 )
    answer=game[m][fortune]
      
    print "Case #%d: %s" % (i, answer)
    i+=1
    