import fileinput
f = fileinput.input()

from functools import reduce
from operator import mul
def product(list):
    return reduce(mul, list, 1)

import numpy

def score(P, K):
    """Probability at least K success"""
    #if K == len(P):
    #    return product(P)

    N = len(P)
    table = numpy.zeros((N+1,N+1)) # table[i,j] is probability that of the first i trials, exactly j are successful
    table[0,0] = 1
    for i in range(1,N+1):
        p = P[i-1]
        for j in range(1, N+1):
            table[i, j] =  p * table[i-1, j-1] + (1-p) * table[i-1, j]

    return numpy.sum(table[len(P),K:])

T = int(f.readline())
for case in range(1, T+1):
    N, K = (int(x) for x in f.readline().split())
    U = float(f.readline())
    P = [float(x) for x in f.readline().split()]
    assert len(P) == N

    P.sort(reverse=True)
    while U and min(P[:K]) < 1:
        min_p = min(P[:K])
        next_min = min(p for p in P[:K]+[1] if p != min_p)
        indexes_to_bump = [i for i in range(K) if P[i] == min_p]

        bump = next_min - min_p
        bump = min(bump, U / len(indexes_to_bump))
        if bump == 0:
            break

        for i in indexes_to_bump:
            P[i] += bump
            U -= bump

    while U and min(P) < 1:
        min_p = min(P)
        next_min = min(p for p in P+[1] if p != min_p)
        
        indexes_to_bump = [i for i in range(N) if P[i] == min_p]

        bump = next_min - min_p
        bump = min(bump, U / len(indexes_to_bump))
        if bump == 0:
            break

        for i in indexes_to_bump:
            P[i] += bump
            U -= bump
    else:
        assert min(P) == 1 or U == 0

    solution = score(P, K)
    print(f"Case #{case}: {solution}")
