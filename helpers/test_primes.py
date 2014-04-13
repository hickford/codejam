#!python3

from .primes import Primes

class TestPrimes:
    """Unit tests for execution with py.test"""
    first_ten_primes = [2,3,5,7,11,13,17,19,21,23]
    
    def test_getitem(self):
        primes = Primes()
        assert primes[0] == 2
        assert primes[9] == 23

    def test_contains(self):
        primes = Primes()
        assert 23 in primes

    def test_getitem_slice(self):
        primes = Primes()
        assert primes[:10] == self.first_ten_primes

    def test_iter(self):
        primes = Primes()
        for p, q in zip(primes, self.first_ten_primes):
            assert p == q

    def test_count(self):
        primes = Primes()
        assert primes.count(100) == 25
        assert primes.count(self.first_ten_primes[-1]) == 10
