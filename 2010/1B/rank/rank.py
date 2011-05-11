#!python
# http://code.google.com/codejam/contest/dashboard?c=635101#s=p2
import copy
from collections import deque
from optparse import OptionParser
usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()

modulus = 100003

class memoize:
  def __init__(self, function):
    self.function = function
    self.memoized = {}

  def __call__(self, *args):
    try:
      return self.memoized[args]
    except KeyError:
      self.memoized[args] = self.function(*args)
      return self.memoized[args]
	
def pure(S,n):
	"""test if n is pure with respect to S"""
	j=n
	try:
		while j > 1:
			j = S.index(j)+1
	except ValueError:
		return False
	return True

subsets = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]

def answer(n):
	count = 0
	for S in subsets(range(2,n)):
		if pure(S+[n],n):
			count += 1
	return count % modulus
	return count
	
@memoize
def F(n,m):
	"""generalised Fibonaci numbers, defined for n>=-1 and m>=0"""
	if n == 0:
		return 1
	elif n<0 or m==0:
		return 0
	else:
		return sum(F(n-j,m) for j in range(1,m+1)) % modulus
	
def diagonal(N):
	"""return diagonal sum"""
	return sum(F(j,N-j) for j in range(0,N+1) ) % modulus

def answer2(N):
	return diagonal(N-1)

#for n in range(500):
#	answer2(n)	# avoid too much recursion
import sys
#print sys.getrecursionlimit()
sys.setrecursionlimit(10**6)
	
if not args:
	parser.error("input omitted")
f = open(args[0])
T = int(f.readline())

for i in range(1,T+1):
	n=int(f.readline().strip() )
	print "Case #%d: %d" % (i,answer2(n))
