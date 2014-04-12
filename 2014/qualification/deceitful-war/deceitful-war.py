#!python3
"""Google Code Jam Qualification Round 2014 Problem D. Deceitful War
https://code.google.com/codejam/contest/2974486/dashboard#s=p3
Naomi and Ken sometimes play games together. Before they play, each of them gets N identical-looking blocks of wood with masses between 0.0kg and 1.0kg (exclusive). All of the blocks have different weights. There are lots of games they could play with those blocks, but they usually play something they call War. Here is how War works:"""

import bisect

def war(naomi, ken):
    assert len(naomi) == len(ken)
    ken = sorted(ken)
    
    naomi_score = 0

    while naomi or ken:
        left = naomi.pop() # Naomi takes any block.

        # Ken plays his smallest block that exceeds Naomi's, else his very smallest block
        j = bisect.bisect_left(ken, left)
        try:
            right = ken.pop(j)
        except IndexError:
            right = ken.pop(0)

        naomi_score += left > right

    return naomi_score


def deceitful_war(naomi, ken):
    assert len(naomi) == len(ken)
    ken = sorted(ken)
    naomi = sorted(naomi)

    naomi_score = 0

    while naomi or ken:
        # naomi plays to win if she can, else uses her smallest block to rid bob of his largest
        left = naomi.pop(-1) if naomi[-1] > ken[-1] else naomi.pop(0)
        right = ken.pop(-1) # Naomi also overestimates her winning blocks, to rid Bob of his best! This is crucial.

        naomi_score += left > right

    return naomi_score


if __name__ == "__main__":
    """The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing a single integer N, the number of blocks each player has. Next follows a line containing N space-separated real numbers: the masses of Naomi's blocks, in kg. Finally there will be a line containing N space-separated real numbers: the masses of Ken's blocks, in kg."""
    import fileinput
    f = fileinput.input()

    T = int(f.readline())
    for case in range(1,T+1):
        N = int(f.readline())
        naomi = [float(x) for x in f.readline().split()]
        ken = [float(x) for x in f.readline().split()]
        assert len(naomi) == len(ken) == N
        y = deceitful_war(naomi, ken)
        z = war(naomi, ken)
        print("Case #{0}: {1} {2}".format(case, y, z))


