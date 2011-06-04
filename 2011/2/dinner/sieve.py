#!/usr/bin/python
from __future__ import division
import math

def primes(n = None, primelist = [2]):
	"""The Sieve of Erastothenes

	Iterator. Yield primes [less than or equal to n]"""
	for p in primelist:
		if n and p > n:
			raise StopIteration
		yield p

	x = primelist[-1]+1
		
	while not n or x <= n:
		limit = int(math.sqrt(x))
		for p in primelist:
			if p > limit:
				# x is prime
				primelist.append(x)
				yield x
				break
			if x % p == 0:
				# x is composite
				break
		x += 1

def sieve(n):
	"""Return primes less than or equal to n"""
	return list(primes(n))

def first_primes(n):
	"""Return first n primes"""
	primelist = []
	fountain = primes()
	n = int(n)
	while len(primelist) < n:
		primelist.append(fountain.next())
	return primelist

def PNT_estimate(n):
	"""Estimate number of primes less than n by n / log(n)"""
	return n / math.log(n)

if __name__ == "__main__":
	""" compare \u03C0(n) against n/log(n)"""
			
	S = [10**2,10**3,10**4,10**5,10**6]

	print "n".ljust(8),u"\u03C0(n)".ljust(7),"n/log(n)".ljust(8),"relative error".ljust(8)
	
	for n in S:
		count = len(sieve(n))
		estimate = PNT_estimate(n)
		relativeError = ( estimate - count ) / count

		print ("%d" % n).rjust(8), ("%d" % count).rjust(7),  ("%d" % round(estimate)).rjust(8), ("%.2g" % relativeError).rjust(8)
		
