# https://code.google.com/codejam/contest/dashboard?c=3264486#s=p0
"""Last year, the Infinite House of Pancakes introduced a new kind of pancake. It has a happy face made of chocolate chips on one side (the "happy side"), and nothing on the other side (the "blank side").

You are the head cook on duty. The pancakes are cooked in a single row over a hot surface. As part of its infinite efforts to maximize efficiency, the House has recently given you an oversized pancake flipper that flips exactly K consecutive pancakes. That is, in that range of K pancakes, it changes every happy-side pancake to a blank-side pancake, and vice versa; it does not change the left-to-right order of those pancakes.

You cannot flip fewer than K pancakes at a time with the flipper, even at the ends of the row (since there are raised borders on both sides of the cooking surface). For example, you can flip the first K pancakes, but not the first K - 1 pancakes.

Your apprentice cook, who is still learning the job, just used the old-fashioned single-pancake flipper to flip some individual pancakes and then ran to the restroom with it, right before the time when customers come to visit the kitchen. You only have the oversized pancake flipper left, and you need to use it quickly to leave all the cooking pancakes happy side up, so that the customers leave feeling happy with their visit.

Given the current state of the pancakes, calculate the minimum number of uses of the oversized pancake flipper needed to leave all pancakes happy side up, or state that there is no way to do it."""

def solve(p, K):
    flipper = 2**K - 1

    flips = 0
    while p >= flipper:
        if p % 2 == 0:
            p //= 2
        else:
            flips += 1
            p ^= flipper

    return "IMPOSSIBLE" if p else flips

import fileinput
f = fileinput.input()

T = int(f.readline())
for case in range(1, T+1):
    S, K = f.readline().split()
    K = int(K)
    n = len(S)
    p = int(S.replace('+', '0').replace('-', '1'), 2)
    solution = solve(p, K)
    print(f"Case #{case}: {solution}")
