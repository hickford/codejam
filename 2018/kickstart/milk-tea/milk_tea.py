# https://code.google.com/codejam/contest/4394486/dashboard#s=p1
"""The milk tea in China is very delicious. There are many binary ("either-or") options for customizing a milk tea order, such as "with ice"/"no ice", "with sugar"/"no sugar", "with bubbles"/"no bubbles", "with pudding"/"no pudding", and so on. A customer's preferences for their milk tea can be represented as a binary string. For example, using the four properties above (in the order they are given), the string 1100 means "with ice, with sugar, no bubbles, no pudding".

Today, Shakti is on duty to buy each of his N friends a milk tea, at a shop that offers P binary options. But after collecting everyone's preferences, Shakti found that the order was getting too complicated, so Shakti has decided to buy the same type of milk tea for everyone. Shakti knows that for every friend, for every preference that is not satisfied, they will complain once. For example, if two of the friends have preferences for types 101 and 010, and Shakti chooses type 001, then the first friend will complain once and the second friend will complain twice, for a total of three complaints.

Moreover, there are M different forbidden types of milk tea that the shop will not make, and Shakti cannot choose any of those forbidden types.

What is the smallest number of complaints that Shakti can get?"""

from math import inf

def complaints(tea, preferences):
    count = 0
    for preference in preferences:
        count += bin(tea^preference).count("1")
    return count

def cost(tea, preferences, forbiddens):
    return inf if tea in forbiddens else complaints(tea, preferences)

def optimal(preferences):
    complaints2 = lambda tea: complaints(tea, preferences)

    best = 0
    bit = 1
    bound = max(preferences)
    while bit <= bound:
        if complaints2(best^bit) < complaints2(best):
            best = best ^ bit
        bit *= 2

    return best

from itertools import combinations
from operator import xor
from functools import reduce

def solve(preferences, forbidden, P):
    best = optimal(preferences)
    candidates = []
    adjustments = [2**i for i in range(P)]
    simultaneous_adjustments = 0
    while len(candidates) < 101 and simultaneous_adjustments <= P:
        for combination in combinations(adjustments, simultaneous_adjustments):
            candidates.append(reduce(xor, combination, best))
        simultaneous_adjustments += 1

    cost2 = lambda tea: cost(tea, preferences, forbidden)
    best_legal = min(candidates, key=cost2)
    return cost(best_legal, preferences, forbidden)

if __name__ == "__main__":
    """The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing 3 integers N, M, and P, as described above. Then, there are N more lines, each of which contains a binary string; these represent the preferences of the N friends. Finally, there are M more lines, each of which contains a binary string; these represent the forbidden types of milk tea that the shop will not make. Binary strings consist only of 0 and/or 1 characters."""
    import fileinput
    f = fileinput.input()
    N = int(f.readline())
    for case in range(1, N+1):
        N, M, P = (int(x) for x in f.readline().split())
        preferences = [int(f.readline(), base=2) for _ in range(N)]
        forbidden = [int(f.readline(), base=2) for _ in range(M)]
        solution = solve(preferences, forbidden, P)
        print(f"Case #{case}: {solution}")        



