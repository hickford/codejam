#!python
# http://code.google.com/codejam/contest/dashboard?c=544101#s=p0
import sys
from optparse import OptionParser
from collections import deque
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

def winners(board,N,K):
    W = set()
    for i in range(N):
        for j in range(N):
            x = board[i][j]
            if x == ".":
                continue
            # look down
            if i+(K-1) <= N-1 and len( set( board[i+r][j] for r in range(K) ) ) == 1:
                W.add(x)
            # look right
            if j+(K-1) <= N-1 and len( set( board[i][j+r] for r in range(K) ) ) == 1:
                W.add(x)
            # look right down
            if i+(K-1) <= N-1 and j+(K-1) <= N-1 and len( set( board[i+r][j+r] for r in range(K) ) ) == 1:
                W.add(x)
            # look left down
            if i+(K-1) <= N-1 and j-(K-1) >= 0 and len( set( board[i+r][j-r] for r in range(K) ) ) == 1:
                W.add(x)                
    return W

def rotate(board,N):
    """Rotate board clockwise"""
    # not yet tested
    board2 = board
    for i in range(N):
        for j in range(N):
            board2[j][(N-1)-i] = board[i][j]
    return board2

def rightGravity(board):
    board2 = []
    for row in board:
        row2 = [x for x in row if x != '.']
        row2 = ['.'] * (len(row)-len(row2)) + row2
        board2.append(row2)
    return board2
    
   
for i in range(1,T+1):
    N, K = [int(x) for x in f.readline().split()]
    board = list()
    for j in range(N):
        board.append( list(f.readline().strip()) )
        
    # board[i][j] is row, column
    board2 = rightGravity(board)
    W = winners(board2,N,K)
    if 'R' in W and 'B' in W:
        answer = "Both"
    elif 'R' in W:
        answer = "Red"
    elif 'B' in W:
        answer = "Blue"
    elif len(W) == 0:
        answer = "Neither"
    else:
        raise Exception, ":("
    print "Case #%d: %s" % (i,answer)

    