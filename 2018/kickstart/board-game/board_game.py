# https://code.google.com/codejam/contest/4394486/dashboard#s=p2
"""Bahu is playing a board game with Bala. Each player has 3 * N army cards with various strength values. There are 3 battlefields in the game. Each player must distribute their cards among the battlefields, face down, such that each battlefield gets exactly N of their cards.

When the game begins, all cards will be revealed. For each battlefield, each player sums up the strength values of their N cards in that battlefield, and then the players compare those totals. If one player has a higher total, that player wins that battlefield. If the totals are the same, Bala wins that battlefield; this is his special advantage.

The overall winner of the game is the player who wins the most battlefields. (Since there are 3 battlefields, it is guaranteed that there will not be an overall tie.)

Bala thinks that his advantage is enough to make him win, so he just randomly shuffles his cards and puts the first N on the first battlefield, the next N on the second battlefield, and the last N on the third battlefield.

Even though Bahu is at a disadvantage, he is still going to try to win! Find the probability that he will win if he distributes his cards optimally. Note that all Bala's cards are faced down so Bahu must choose the distribution of his cards before seeing the distribution of Bala's cards."""

from itertools import permutations
from sys import stderr

def to_battlefields(cards):
    N = len(cards) // 3
    return (cards[0:N], cards[N:2*N], cards[2*N:3*N])

def hickford_preference(battlefields):
    # prefer medium-medium-small shape, with mediums as equal as possible
    return sum(battlefields[0])+sum(battlefields[1]), -abs(sum(battlefields[0]) - sum(battlefields[1]))

def solve(A, B):
    # A = sorted(A, reverse=True)
    # N = len(cards) // 3
    possible_battlefields = map(to_battlefields, permutations(A))
    A_battlefields = max(possible_battlefields, key=hickford_preference)
    print(A_battlefields, file=stderr)
    return prob_victory(A_battlefields, B)

def victory(A_battlefields, B_battlefields):
    return sum(sum(A) > sum(B) for A,B in zip(A_battlefields, B_battlefields)) >= 2

def prob_victory(A_battlefields, B):
    N = len(B) // 3
    count = 0
    victories = 0
    for permutation in permutations(B):
        B_battlefields = to_battlefields(permutation)
        if victory(A_battlefields, B_battlefields):
            victories += 1
        count += 1

    return victories / count

if __name__ == "__main__":
    """The first line of the input gives the number of test cases, T. T test cases follow; each consists of three lines. The first line contains an integer N, as described above. The second line contains 3 * N integers A0, A1, ... , A3*N-1, representing the strength values of Bahu's cards. The third line consists of 3 * N integers B0, B1, ... , B3*N-1, representing the strength values of Bala's cards."""
    import fileinput
    f = fileinput.input()
    N = int(f.readline())
    for case in range(1, N+1):
        N = int(f.readline())
        A = [int(x) for x in f.readline().split()] # Bahu (us)
        B = [int(x) for x in f.readline().split()] # Bala (opponent)
        assert len(A) == len(B) == 3*N
        solution = solve(A, B)
        print(f"Case #{case}: {solution}")        
