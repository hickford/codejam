#!python3
from codejamhelpers import Primes

class TestPrimes:
    """Unit tests for execution with py.test"""
    first_ten_primes = [2,3,5,7,11,13,17,19,23,29]
    
    def test_getitem(self):
        primes = Primes()
        assert primes[0] == 2
        assert primes[9] == self.first_ten_primes[9]
        assert primes[5] == self.first_ten_primes[5]

    def test_contains(self):
        primes = Primes()
        assert 31 in primes
        assert 29 in primes
        assert 25 not in primes
        assert 100 not in primes

    def test_getitem_slice(self):
        primes = Primes()
        assert primes[:10] == self.first_ten_primes
        assert primes[:5] == self.first_ten_primes[:5]

    def test_iter(self):
        primes = Primes()
        for p, q in zip(primes, self.first_ten_primes):
            assert p == q

    def test_count(self):
        primes = Primes()
        assert primes.count(29) == 10
        assert primes.count(100) == 25
        assert primes.count(29) == 10
