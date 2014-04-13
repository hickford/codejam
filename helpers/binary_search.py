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

def minimise_convex(f):
    """Given a U-shaped (convex and eventually increasing) function f, find its minimum over the non-negative integers. That is m such that f(m) <= f(n) for all n."""
    f_prime = lambda n: (f(n) - f(n-1)) if n > 0 else 0
    return binary_search(f_prime, 0)

assert minimise_convex(lambda x: (x-5)**2) == 5
assert minimise_convex(lambda x: x) == 0

def kth_root(n, k):
    """Calculate the greatest non-negative integer r such that r**k <= n."""
    return binary_search(lambda x: x**k, n)

assert kth_root(125, 3) == 5
