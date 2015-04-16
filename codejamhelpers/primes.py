#!python3
import bisect

class Primes:
    """The prime numbers. Lazy evaluation."""
    def __init__(self, frontier = None):
        self.primes = [2]   # primes found so far
        self.frontier = 3   # least number we haven't tested for primality
        if frontier:
            self._explore_to_bound(frontier-1)

    def __repr__(self):
        return "Primes(frontier={0})".format(self.frontier)

    def __str__(self):
        return "{0} primes up to {1}".format(len(self.primes), self.primes[-1])

    def _explore_to_bound(self, bound):
        if bound < self.frontier:
            return 

        x = self.frontier
        assert x % 2 == 1

        while x <= bound:
            for p in self.primes:
                if p**2 > x:
                    self.primes.append(x)
                    break
                if x % p == 0:
                    # x is composite
                    break

            x += 2

        self.frontier = x

    def _explore_to_index(self, index):
        x = self.frontier 
        assert x % 2 == 1

        while len(self.primes) < index + 1:
            for p in self.primes:
                if p**2 > x:
                    self.primes.append(x)
                    break
                if x % p == 0:
                    # x is composite
                    break

            x += 2

        self.frontier = x

    def __getitem__(self, i):
        """The ith prime"""
        if isinstance(i, slice):
            index = i.stop - 1
        else:
            index = i

        self._explore_to_index(index)
        return self.primes[i]

    def __contains__(self, n):
        """Test whether n is a prime"""
        self._explore_to_bound(n)
        i = bisect.bisect_left(self.primes, n)
        return i < len(self.primes) and self.primes[i] == n

    def count(self, x):
        """Count the number of primes less than or equal to x"""
        self._explore_to_bound(x)
        return bisect.bisect(self.primes, x)
