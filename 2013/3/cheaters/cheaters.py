#!python3
"""Google Code Jam Round 3 2013 Problem A. Cheaters
https://code.google.com/codejam/contest/2433487/dashboard#s=p0
You've been playing roulette for a while in a local casino. Roulette is a simple casino game in which multiple players place bets on one or more numbers between 0 and 36 (inclusive). Next, a wheel is spun in one direction with a ball spinning in the other direction. The roulette wheel contains the same numbers 0 to 36. Some real roulette wheels also have a space labeled 00, but ours does not. Eventually, the ball falls on one of the numbers. If a player placed a bet on that particular number, he receives 36 times his bet (so the profit of that bet is 35 times the bet). All bets placed on other numbers lose.

Unfortunately, luck hasn't been on your side, and you have been losing all night long. At one point, you started to wonder whether the roulette game was fair or not, and after observing the game some more, you noticed a pattern that must be profitable for the casino: the ball always lands on one of the numbers that has the least total money bet on it! If multiple numbers tie for the least total money bet, the ball lands on one of those uniformly at random.

Of course, you'll be notifying the authorities about this foul play, but first you want to win your money back by exploiting your new-found knowledge. To do so, you wait until all other players have placed their bets and then place bets of your own. Unfortunately, you have a limited budget left, so you cannot bet more than that. You are allowed to bet on zero or more different numbers, and each of those bets can be any positive integer amount (perhaps with different amounts for different numbers), so as long as the sum of your bets does not exceed your budget. What is the maximum expected profit you can make?"""

import numpy as np

def calculate_expected_profit(my_bets, totals, odds_against = None):
    """Calculate the expected profit"""
    if odds_against == None:
        odds_against = len(totals) - 1

    assert len(my_bets) == len(totals)
    assert np.all(my_bets <= totals)

    min_total = np.min(totals)
    winning_bets = (totals == min_total)
    my_winning_bets = my_bets * winning_bets 
    return -np.sum(my_bets) + odds_against * np.sum(my_winning_bets) / np.sum(winning_bets)

# unit tests
assert calculate_expected_profit([1,1,2],[3,2,2]) == -4 + 2 * (0.5 * 1 + 0.5 * 2)

def solve(budget, others_bets, size):
    others_bets = sorted(others_bets, reverse=True)
    totals = np.zeros(size)
    for i, x in enumerate(others_bets):
        totals[i] = x

    my_bets = np.zeros_like(totals)

    best_so_far = calculate_expected_profit(my_bets, totals)
    assert best_so_far == 0

    i = 0
    while np.sum(my_bets) < budget:
        min_total = np.min(totals)

        if totals[i] == min_total:
            my_bets[i] += 1
            totals[i] += 1

            profit = calculate_expected_profit(my_bets, totals)
            if profit > best_so_far:
                best_so_far = profit

        i += 1
        i %= len(totals)

    assert np.sum(my_bets) + np.sum(others_bets) == np.sum(totals)
    assert np.sum(my_bets) <= budget
    return best_so_far

if __name__ == "__main__":
    """The first line of input gives the number of cases, T. T test cases follow. Each test case consists of two lines. The first line contains two integers: the budget you still have, B, and the number of numbers other players have placed bets on, N. The second line contains N integers Xi, the total amounts of money bet by other players on each of those different numbers."""
    import fileinput
    f = fileinput.input()

    T = int(f.readline())
    for case in range(1,T+1):
        B, N = [int(x) for x in f.readline().split()]
        Xs = [int(x) for x in f.readline().split()]
        assert len(Xs) == N <= 37
        answer = solve(B, Xs, 37)
        print("Case #{0}: {1}".format(case, answer))



