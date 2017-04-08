# https://code.google.com/codejam/contest/dashboard?c=3264486#s=p1
"""Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?"""

import fileinput
f = fileinput.input()

def is_tidy(n):
    s = str(n)
    return "".join(sorted(s)) == s

assert is_tidy(224488)
assert not is_tidy(495)

def solve(N):
    solution = ""
    hit = False

    for digit in str(N):
        if hit:
            digit = "9"

        if solution == "" or digit >= solution[-1]:
            solution += digit
        else:
            solution = str(int(solution) - 1)
            hit = True
            solution += "9"

    solution = int(solution)
    if is_tidy(solution):
        return solution

    return solve(solution)

T = int(f.readline())
for case in range(1, T+1):
    N = int(f.readline())
    solution = solve(N)
    print(f"Case #{case}: {solution}")
