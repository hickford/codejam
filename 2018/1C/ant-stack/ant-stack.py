# https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard/000000000003e0a8
"""Scott has an ant farm containing N ants. Each ant has a certain length and weight.

Today, as a challenge for the ants, Scott has placed some food at the top of the ant farm. The ants will try to reach it by arranging themselves into a vertical stack, with each ant in the stack directly holding the next on its back. In this way, each ant bears the weight of all ants above it. Scott's ants are very strong for their size and are able to carry up to 6 times their own weight. For example, an ant that weights 8 milligrams can carry two other ants weighing 24 milligrams each! Each ant also has a body length; the exact lengths are not important, except that they are all different.

The stack must be linear. Each ant except for the top ant must be directly below exactly one ant, and each ant except for the bottom ant must be directly above exactly one ant.
The lengths of the ants in the stack must be strictly decreasing from the bottom to the top of the stack; this ensures that each new ant that joins the stack will be able to climb up to the top.
For each ant, the sum of the weights of all the ants above it in the stack must be no more than 6 times the weight of that ant.
What is the maximum number of these ants that can form such a stack?"""

from sys import stderr, argv
from itertools import accumulate
import math

try:
    import numpy
except ImportError:
    numpy = None

def solve_vanilla(W):
    N = len(W)
    capacity = [6*w for w in W]
    inf = math.inf

    # let S[h][i] be minimum weight of stack height h with ant i at base
    S = W # S_1
    def mapper(w, b, c):
        return w + b if b <= c else inf 
    h = 0
    while min(S) < inf:
        h += 1
        T = [inf] + list(accumulate(S, min)) # T[i] = minimum weight of stack height h-1 with some ant j < i at base
        S = list(map(mapper, W, T, capacity))
        # print(S, file=stderr)

    return h

def solve_with_numpy(W):
    W = numpy.array(W, dtype=numpy.int64) 
    capacity = 6*W
    inf = numpy.iinfo(numpy.int64).max

    # let S[h][i] be minimum weight of stack height h with ant i at base
    S = W # S_1
    h = 0
    while numpy.min(S) < inf:
        h += 1
        T = numpy.minimum.accumulate(S)
        T = numpy.roll(T, 1)
        T[0] = inf
        S = numpy.where(T <= capacity, W + T, inf)
        # print(S, file=stderr)

    return h

solve = "--numpy" in argv and solve_with_numpy or "--vanilla" in argv and solve_vanilla or (solve_with_numpy if numpy else solve_vanilla)

T = int(input())
for case in range(1, T+1):
    N = int(input())
    W = [int(x) for x in input().split()]
    assert len(W) == N

    solution = solve(W)
    print("Case #{}: {}".format(case, solution))
