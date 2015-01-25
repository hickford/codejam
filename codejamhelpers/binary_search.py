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

def minimise_convex(f):
    """Given a U-shaped (convex and eventually increasing) function f, find its minimum over the non-negative integers. That is m such that f(m) <= f(n) for all n. If there exist multiple solutions, return the largest. Uses binary search on the derivative."""
    f_prime = lambda n: (f(n) - f(n-1)) if n > 0 else 0
    return binary_search(f_prime, 0)


def minimise_convex2(f):
    """Given a U-shaped (convex and eventually increasing) function f, find its minimum over the non-negative integers. That is m such that f(m) <= f(n) for all n. If there exist multiple solutions, return the largest. Uses ternary search."""
    for n in powers_of_two():
        if f(n) > f(n//2):
            break
            
    upper = n
    lower = n//4

    while upper > lower + 1:
        upper_third = (lower + 2*upper)//3
        lower_third = max((2*lower + upper)//3, lower + 1)
        if f(upper_third) > f(lower_third):
            upper = upper_third
        else:
            lower = lower_third

    assert f(lower) < f(lower+1)
    return lower


def kth_root(n, k):
    """Calculate the greatest non-negative integer r such that r**k <= n."""
    return binary_search(lambda x: x**k, n)

