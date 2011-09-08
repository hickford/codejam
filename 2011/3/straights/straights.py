#!python
# Dire Straights http://code.google.com/codejam/contest/dashboard?c=1158485#s=p1
import fileinput
f = fileinput.input()
T = int(f.readline())

for i in range(1,T+1):
    line = [int(x) for x in f.readline().split()]
    N = line[0]
    cards = sorted(line[1:])
    assert len(cards) == N
    #print cards
    straights = []
    for x in cards:
        for straight in reversed(straights):
            if straight[-1] == x-1:
                straight.append(x)
                break
        else:
            straight = [x]
            straights.append(straight)
        #print straights
    answer = 0
    if straights:
        answer = min(len(straight) for straight in straights)
    print "Case #%d: %s" % (i,answer)
