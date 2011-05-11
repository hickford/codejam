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
	profit = 0
	profits = {0:0}
	first,second = f.readline(),f.readline()
	r,k,n = [int(x) for x in first.split()]
	groups = [int(x) for x in second.split()]
	assert len(groups) == n
	#print k
	queue = deque(groups)
	initial = copy.copy(queue)	# important
	states = [(0,initial)]
	ride = 1
	while ride <= r:
		#car = []
		car2 = 0
		count = 0
		for x in queue:
			if x > k - car2:
				break
			#car.append(x)
			car2 += x
			count += 1
		#assert sum(car) == car2
		profit += car2
		#print queue,car
		queue.rotate(-count)
		#if queue == initial:
		#	repeat = (r-ride)//ride
		#	profit += profit*repeat
		#	ride += ride*repeat
		for when,before in states:
			if queue == before:
				interval = ride - when
				repeat = (r-ride)//interval
				profit += (profit - profits[when])*repeat
				ride += interval * repeat
				break
		ride += 1
		states.append( (ride,copy.copy(queue)) )
		profits[ride] = profit
	print "Case #%d: %d" % (i,profit)
	#print