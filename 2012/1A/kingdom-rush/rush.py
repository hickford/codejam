#!python
# http://code.google.com/codejam/contest/1645485/dashboard#s=p1

import fileinput
f = fileinput.input()
T = int(f.readline())

def solve(levels):
    levels = sorted(levels,key = lambda level: level[1])
    N = len(levels)
    
    played = 0
    stars = 0
    
    while levels:
        # play a 2-star level if we can
        if levels[0][1] <= stars:
            level = levels.pop(0)
            played += 1
            
            if level[0] == None:
                stars += 1
            else:
                stars += 2
            
            continue
            
        # otherwise, ask which 1-star levels can we play
        one_star_indices = [i for i,level in enumerate(levels) if level[0] <= stars and level[0] != None]
        
        if one_star_indices:
            # play the 1-star level with hardest 
            i = one_star_indices[-1]    # play accessible level with 
            levels[i][0] = None         # mark this 1-star level unplayable
            
            played += 1
            stars += 1
            continue
            
        return False
        
        
        
            
    return played
        
        
        
        
    
    

for case in range(1,T+1):
    N = int(f.readline())
    
    levels = list()
    
    for i in range(N):
        a,b = [int(x) for x in f.readline().split()]
        levels.append( [a,b] )
        
    answer = solve(levels)
    if answer == False:
        answer = "Too Bad"
        
    print "Case #%d: %s" % (case, answer)