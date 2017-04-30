import fileinput
f = fileinput.input()

from functools import reduce
from operator import mul
def product(list):
    return reduce(mul, list, 1)


T = int(f.readline())
for case in range(1, T+1):
    N, K = (int(x) for x in f.readline().split())
    U = float(f.readline())
    P = [float(x) for x in f.readline().split()]
    assert len(P) == N

    while U and min(P) < 1:
        min_p = min(P)
        next_min = min(p for p in P+[1] if p != min_p)
        
        indexes_to_bump = [i for i in range(N) if P[i] == min_p]

        bump = next_min - min_p
        bump = min(bump, U / len(indexes_to_bump))

        assert bump > 0

        for i in indexes_to_bump:
            P[i] += bump
            U -= bump

    assert min(P) == 1 or U == 0

    solution = product(P)
    print(f"Case #{case}: {solution}")
