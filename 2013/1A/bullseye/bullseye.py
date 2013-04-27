#!python
# https://code.google.com/codejam/contest/2418487/dashboard#s=p0
# Maria has been hired by the Ghastly Chemicals Junkies (GCJ) company to help them manufacture bullseyes. A bullseye consists of a number of concentric rings (rings that are centered at the same point), and it usually represents an archery target. GCJ is interested in manufacturing black-and-white bullseyes. 

from __future__ import division
import math

def f(n,r):
	"""Area of bullseye with n rings, inner radius r, as a multiple of pi."""
	return 2*n**2 + n*(2*r-1)

def solve2(r,t):
	"""Solve using quadratic equation"""
	import gmpy
	from gmpy import mpz

	a = 2
	b = 2*r - 1
	c = -t

	x = (-b + mpz(b**2 - 4*a*c).sqrt()) // (2*a) 
	return int(x)

assert f(0,0) == 0
assert f(0,1) == 0
assert f(1,0) == 1
assert f(1,1) == 3
assert f(2,0) == 1+5
assert f(2,1) == 3+7
assert f(2,2) == 5+9
assert f(3,0) == 1+5+9
assert f(3,1) == 3+7+11

def solve(r,t):
	"""Maximum number of black rings that Maria can draw, with inner radius r, given pi*t of paint.."""
	return binary_search(lambda n: f(n, r), t)

def binary_search(f, t):
	"""Find the greatest positive integer n such that f(n) <= t , assuming f is increasing. By binary search. Or return 0 if f(1) > t"""
	if f(1) > t:
		return 0

	n = 1

	while f(n) <= t:
		lower = n	# Can draw this many rings
		n *= 2
	else:
		upper = n	# Can't draw this many rings

	assert lower < upper

	while upper > lower+1:
		mid = (upper + lower) // 2
		if f(mid) <= t:
			lower = mid
		else:
			upper = mid

	assert upper == lower+1
	return lower

assert binary_search(lambda x: x, 6) == 6
assert binary_search(lambda x: x**2, 10) == 3
assert binary_search(lambda x: x+10, 5) == 0



if __name__ == "__main__":
	import fileinput
	stdin = fileinput.input()

	T = int(stdin.readline())

	for case in range(1,T+1):
		r,t = [int(x) for x in stdin.readline().split()]
		answer = solve(r,t)
		assert answer == solve2(r,t)
		print "Case #%d: %s" % (case, answer)
