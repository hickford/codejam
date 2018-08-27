# https://code.google.com/codejam/contest/4394486/dashboard#s=p0
"""Yogurt can be a nutritious part of an appetizer, main course, or dessert, but it must be consumed before it expires, and it might expire quickly! Moreover, different cups of yogurt might expire on different days.

Lucy loves yogurt, and she has just bought N cups of yogurt, but she is worried that she might not be able to consume all of them before they expire. The i-th cup of yogurt will expire Ai days from today, and a cup of yogurt cannot be consumed on the day it expires, or on any day after that.

As much as Lucy loves yogurt, she can still only consume at most K cups of yogurt each day. What is the largest number of cups of yogurt that she can consume, starting from today?"""

def solve(expiries, K):
    expiries = sorted(expiries)
    day = 0
    appetite = K
    consumed = 0
    for expiry in expiries:
        if day < expiry:
            consumed += 1
            appetite -= 1
            if appetite == 0:
                appetite = K
                day += 1
    return consumed

if __name__ == "__main__":
    """The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with one line containing two integers N and K, as described above. Then, there is one more line with N integers Ai, as described above."""
    import fileinput
    f = fileinput.input()

    N = int(f.readline())
    for case in range(1, N+1):
        N, K = (int(x) for x in f.readline().split())
        assert 1 <= K <= N
        A = [int(x) for x in f.readline().split()]
        assert len(A) == N
        solution = solve(A, K)
        print(f"Case #{case}: {solution}")
