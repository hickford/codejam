# https://code.google.com/codejam/contest/dashboard?c=3264486#s=p2
"""A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. The other N stalls are for users.

Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible. To avoid confusion, they follow deterministic rules: For each empty stall S, they compute two values LS and RS, each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(LS, RS) is maximal. If there is only one such stall, they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal. If there are still multiple tied stalls, they choose the leftmost stall among those.

K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.

When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?"""

import heapq
import codejamhelpers
import math

def solve_slow(n, k):
    """Starting with n stalls, size of largest gap after k people enter"""
    gaps = [-n] # use negative keys for max-heap
    for person in range(k):
        gap = abs(heapq.heappop(gaps))
        new_gaps = (gap // 2, (gap - 1) // 2)
        for new_gap in new_gaps:
            heapq.heappush(gaps, -new_gap)

    return abs(heapq.heappop(gaps))

def step(k):
    return 2**codejamhelpers.binary_search(lambda t: 2**t, k+1)

def solve(n, k):
    """Starting with n stalls, size of largest gap after k people enter"""
    if k == 0:
        return n
    correction = step(k)-(k+1)
    return (n+correction)//step(k)

for n in range(1, 100):
    for k in range(0, n+1):
        assert solve(n, k) == solve_slow(n, k), f"{n},{k}"

import fileinput
f = fileinput.input()

T = int(f.readline())
for case in range(1, T+1):
    N, K = (int(x) for x in f.readline().split())
    last_gap = solve(N, K-1)
    solution = f"{last_gap//2} {(last_gap-1)//2}"
    print(f"Case #{case}: {solution}")
