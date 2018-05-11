# https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard/000000000003e0a8
"""Scott has an ant farm containing N ants. Each ant has a certain length and weight.

Today, as a challenge for the ants, Scott has placed some food at the top of the ant farm. The ants will try to reach it by arranging themselves into a vertical stack, with each ant in the stack directly holding the next on its back. In this way, each ant bears the weight of all ants above it. Scott's ants are very strong for their size and are able to carry up to 6 times their own weight. For example, an ant that weights 8 milligrams can carry two other ants weighing 24 milligrams each! Each ant also has a body length; the exact lengths are not important, except that they are all different.

The stack must be linear. Each ant except for the top ant must be directly below exactly one ant, and each ant except for the bottom ant must be directly above exactly one ant.
The lengths of the ants in the stack must be strictly decreasing from the bottom to the top of the stack; this ensures that each new ant that joins the stack will be able to climb up to the top.
For each ant, the sum of the weights of all the ants above it in the stack must be no more than 6 times the weight of that ant.
What is the maximum number of these ants that can form such a stack?"""


# dynamic programming? 
# 
# f[i][h] = with ant i at bottom, minimum weight of stack containing h ants. or infinity if impossible.
# 
# f[i+1][h] = min(w[i+1]+f[k][h-1]) over all k <= i where f[k][h-1] <= 6*w[i+1]
# 
# f[i][h+1] = min(w[i] + f[k][h]) over all k < i where f[k][h] <= 6 * w[i]
# 
# solution = greatest j with some f[i][h] finite
# 
from sys import stderr
from math import inf

T = int(input())
for case in range(1, T+1):
    N = int(input())
    W = [int(x) for x in input().split()]
    assert len(W) == N

    # let S[h][i] be minimum weight of stack height h with ant i at base
    h = 1
    S = W # S_1
    while min(S) < inf:
        T = [inf] * N
        for i in range(N):
            for k in range(0, i):
                if S[k] <= 6 * W[i]:
                    T[i] = min(T[i], W[i] + S[k])
        S = T
        h += 1
        print(S, file=stderr)

    solution = h-1
    print("Case #{}: {}".format(case, solution))
