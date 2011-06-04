#!/usr/bin/python
from __future__ import division

def __test(a,b):
	"""Raise error if a,b not integers or both equal zero """
	if a != int(a) or b != int(b):
		raise Exception("a and b must both be integers")
	if a == 0 and b == 0:
		raise ValueError("a and b must not both equal zero")

def gcd(a,b):
	"""Return greatest common divisor of integers a and b"""
	__test(a,b)
	
	while b != 0:
		(a,b) = (b, a % b)	
	return abs(a)


def bezout(a,b,test=True):
	"""Return (d,x,y) such that d = a*x+b*y = gcd(a,b) """
	if test:
		__test(a,b)

	if b == 0:
		return (abs(a),a//abs(a),0)
	else:
		(q,r) = divmod(a,b)
		(d,x,y) = bezout(b,r,test=False)
		return (d,y,x-y*q)
	

if __name__ == "__main__":
	"""Test algorithms for some pairs"""

	pairs = [
	(2028532369 , 1926605803),
	(1816883927, 1853573797),
	(1992502829 , 1750170271),
	(1672295039, 821350697)
	]

	for (a,b) in pairs:
		(d,x,y) = bezout(a,b)
		print ("%d = %d * %d + %d * %d" % (d,x,a,y,b))
		assert d == x*a + y*b

