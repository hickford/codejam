#!python3

def binary_search(f, t):
    """Given an increasing function f, find the greatest non-negative integer n such that f(n) <= t. If f(n) > t for all n, return None."""
    if f(0) > t:
        return None

    lower = 0
    for n in powers_of_two():
        if f(n) <= t:
            lower = n
        else:
            upper = n
            break

    while upper > lower + 1:
        mid = (upper+lower) // 2
        if f(mid) <= t:
            lower = mid
        else:
            upper = mid

    assert f(lower) <= t < f(lower+1)
    return lower

def powers_of_two():
    n = 1
    while True:
        yield n
        n *= 2

# Unit tests
assert binary_search(lambda n: n, 6) == 6
assert binary_search(lambda n: n**2, 10) == 3
assert binary_search(lambda n: 2*n, 1) == 0
assert binary_search(lambda n: n+10, 5) == None
