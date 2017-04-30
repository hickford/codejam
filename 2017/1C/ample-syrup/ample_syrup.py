import fileinput
from math import pi
from collections import namedtuple

Pancake = namedtuple('Pancake', ['r', 'h'])

f = fileinput.input()

T = int(f.readline())
for case in range(1, T+1):
    N, K = (int(x) for x in f.readline().split())
    pancakes = list()
    for i in range(N):
        r, h = [int(x) for x in f.readline().split()]
        pancakes.append(Pancake(r, h))

    pancakes.sort(key=lambda p: p.r, reverse=True)

    best = 0

    for i in range(N):
        bottom = pancakes[i]
        remainder = pancakes[i+1:]
        remainder.sort(key=lambda p: p.r * p.h, reverse=True)
        stack = [bottom] + remainder[:K-1]
        if len(stack) < K:
            continue
        assert len(stack) == K

        area = pi * bottom.r**2 + 2*pi * sum(p.r * p.h for p in stack)
        best = max(area, best)

    solution = best
    print(f"Case #{case}: {solution}")
