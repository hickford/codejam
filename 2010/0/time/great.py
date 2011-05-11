#!python
from optparse import OptionParser
usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if not args:
	parser.error("input omitted")
f = open(args[0])

def gcd(a,b):
        """Return greatest common divisor of integers a and b"""
        while b != 0:
                (a,b) = (b, a % b)        
        return abs(a)

for i,line in enumerate(f):
	if i == 0:
		continue
	numbers = [int(x) for x in line.split() ]
	n = numbers[0]
	times = numbers[1:]
	times = sorted(set(times))
	differences = [a-b for a in times for b in times if a-b > 0]
	d = reduce(gcd,set(differences))
	#print times,d
	y = (-times[0]) % d
	while True:
		if all ((x+y)%d == 0 for x in times):
			break
		y += d
	print "Case #%d: %d" % (i,y)