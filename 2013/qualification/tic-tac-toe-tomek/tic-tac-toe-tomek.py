#!python
"https://code.google.com/codejam/contest/2270488/dashboard#s=p0"
import fileinput, sys, numpy
f = fileinput.input()

T = int(f.readline())

def solve(board):
    lines = list()
    lines.append(board.diagonal())
    lines.append(board[::-1].diagonal())
    lines.extend(numpy.hsplit(board, 4))
    lines.extend(numpy.vsplit(board, 4))
    
    lines = [list(x.ravel()) for x in lines]
    for line in lines:
        if set(line).issubset(set("XT")):
            return "X won"
        if set(line).issubset(set("OT")):
           return "O won"

    if '.' in board:
        return "Game has not completed"
    
    return "Draw"

for case in range(1,T+1):
    board = numpy.array([list(f.readline().strip()) for i in range(4)])
    #print >> sys.stderr, board
    assert board.shape == (4,4)
    
    
    answer = solve(board)
    print "Case #%d: %s" % (case, answer)
    f.readline()