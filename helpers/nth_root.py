#!python3
from . import binary_search

def kth_root(n, k):
    """Calculate the greatest integer r such that r**k <= n."""
    return binary_search(lambda x: x**k, n)

assert kth_root(125, 3) == 5
