import fileinput
from sys import stderr
f = fileinput.input()
def input():
    return f.readline()

def divide_rounding(p, q):
    return (p + q//2) // q

def percentage(p, q):
    return divide_rounding(100*p, q)

assert percentage(5, 100) == 5
assert percentage(5, 1000) == 1
assert percentage(5, 1001) == 0
assert percentage(6, 1001) == 1

def divide_rounding_up(p, q):
    return (p + q-1) // q

from math import inf

def extra_votes_to_round_up(p, q):
    remainder = p*100 % q
    threshold = (q+1)//2
    if remainder >= threshold:
        return inf
    else:
        return divide_rounding_up(threshold-remainder, 100)

T = int(input())
for case in range(1, T+1):
    N, L = [int(x) for x in input().split()]
    votes = [int(x) for x in input().split()]
    assert len(votes) == L
    assert sum(votes) <= N

    while sum(votes) < N:
        remaining = N - sum(votes)
        if votes[-1] != 0:
            votes.append(0)
        key = lambda i: extra_votes_to_round_up(votes[i], N)
        i = min(range(len(votes)), key=key)
        spend = key(i)
        votes[i] += min(spend, remaining)
        # print(votes, file=stderr)

    solution = sum(percentage(v, N) for v in votes)    
    print("Case #{}: {}".format(case, solution))
    