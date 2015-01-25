#!python3
from .binary_search import binary_search, minimise_convex, minimise_convex2, kth_root

def test_binary_search():
    assert binary_search(lambda n: n, 6) == 6
    assert binary_search(lambda n: n**2, 10) == 3
    assert binary_search(lambda n: 2*n, 1) == 0
    assert binary_search(lambda n: n+10, 5) == None

def test_kth_root():
    assert kth_root(125, 3) == 5

def exercise(find_minimum):
    assert find_minimum(lambda x: (x-5)**2) == 5
    assert find_minimum(lambda x: x) == 0
    assert find_minimum(lambda x: (x-4)*(x-5)) == 5

def test_minimise_convex():
    exercise(minimise_convex)

def test_minimise_convex2():
    exercise(minimise_convex2)