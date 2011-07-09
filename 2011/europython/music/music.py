#!python
# http://code.google.com/codejam/contest/dashboard?c=1277486#s=p1
import sys
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

for i in range(1,T+1):
    N = int(f.readline())
    songs = list()
    for j in range(N):
        song = f.readline().rstrip("\r\n").upper()
        songs.append(song)
    print "Case #%d:" % i
    for song in songs:
        uniques = list()
        for l in range(0,len(song)+1):
            # l is length of substring
            for r in range(0,len(song)+1-l):
                x = song[r:r+l]
                matches = [s for s in songs if x in s]
                if len(matches) == 1:
                    uniques.append(x)
            if uniques:
                break
        if uniques:
            print '"%s"' % min(uniques)
        else:
            print ":("
    # answer in upper case, since lexicographically upper case < lower case