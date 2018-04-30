import fileinput
from sys import stderr
f = fileinput.input()
def input():
    return f.readline()

def percentage(a, b):
    quotient, remainder = divmod(a*100,b)
    if remainder >= (b+1)//2:
        quotient += 1
    return quotient

def how_many_to_make_round_up(a, b):
    quotient, remainder = divmod(a*100,b)
    if remainder >= (b+1)//2:
        return 0
    else:
        return (b+1)//2 - remainder

assert percentage(5, 100) == 5
assert percentage(5, 1000) == 1
assert percentage(5, 1001) == 0
assert percentage(6, 1001) == 1

T = int(input())
for case in range(1, T+1):
    N, L = [int(x) for x in input().split()]
    votes = [int(x) for x in input().split()]
    assert len(votes) == L
    assert sum(votes) <= N

    while sum(votes) < N:
        remaining = N - sum(votes)
        round_downs = [i for i, v in enumerate(votes) if how_many_to_make_round_up(v, N)]
        if votes[-1] != 0:
            votes.append(0)
        if round_downs:
            key = lambda i: how_many_to_make_round_up(votes[i], N)
            i = min(round_downs, key=key)
            spend = key(i)
            if spend <= remaining:
                votes[i] += spend
                continue
        spend = how_many_to_make_round_up(0, N)
        spend = min(spend, remaining)
        votes.append(spend)

    solution = sum(percentage(v, N) for v in votes)    
    print("Case #{}: {}".format(case, solution))
    