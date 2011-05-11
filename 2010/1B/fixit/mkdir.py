#!python
import copy
from collections import deque
from optparse import OptionParser
usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if not args:
	parser.error("input omitted")
f = open(args[0])
T = int(f.readline())

for i in range(1,T+1):
	N,M = ( int(x) for x in f.readline().split() )
	existing = [ f.readline().strip().strip("/").split("/") for j in range(N) ]
	desired = [ f.readline().strip().strip("/").split("/") for j in range(M) ]
	count = 0
	#print N,M,"exist",existing,"desired",desired
	for path in desired:
		y = []
		path2 = path[:]
		while path2:
			y.append(path2.pop(0) )
			#print y
			if y in existing:
				#print "already exists",y
				continue
			else:
				count += 1
				existing.append(y[:])
				#print "mkdir",y
	print "Case #%d: %d" % (i,count)
	#print
	pass