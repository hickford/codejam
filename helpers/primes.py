#!python3

import bisect
from math import sqrt

class Primes:
    """The prime numbers. Lazy evaluation."""
    def __init__(self):
        self.primes = [2]   # primes found so far
        self.frontier = 3   # least number we haven't tested for primality

    def _explore_to_bound(self, bound):
        x = self.frontier
        assert x % 2 == 1

        while x <= bound:
            limit = sqrt(x)

            for p in self.primes:
                if p > limit:
                    self.primes.append(x)
                    break
                if x % p == 0:
                    break

            x += 2

        self.frontier = x

    def _explore_to_index(self, index):
        while len(self.primes) < index:
            _explore_to_bound(self.frontier+2)

    def __getitem__(self, key):
        self._explore_to_index(key)
        return self.primes[key]

    def __iter__(self):
        pass

    def __contains__(self, x):
        self._explore_to_bound(x)
        i = bisect.bisect_left(self.primes, x)
        return self.primes[i] == x

    def count(self, x):
        """Count the number of primes less than or equal to x"""
        self._explore_to_bound(x)
        return bisect.bisect(self.primes, x)
