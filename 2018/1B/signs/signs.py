# The first line of the input gives the number of test cases, T. T test cases follow. Each begins with one line containing one integer S: the number of road signs. Then, S more lines follow. The i-th of these lines represents the i-th sign (in west-to-east order), and contains three integers Di, Ai, and Bi: the sign's distance (in kilometers) east of Signfield, the number on its west side, and the number on its east side.

import fileinput
from sys import stderr
f = fileinput.input()
def input():
    return f.readline()

T = int(input())
for case in range(1, T+1):
    S = int(input())
    data = [[int(x) for x in input().split()] for _ in range(S)]
    D, A, B = list(map(list, zip(*data)))
    possibleMs = set(d + a for d,a in zip(D,A))
    possibleNs = set(d - b for d,b in zip(D,B))
    best_pair = None
    longest_run = 0

    maximal_sequences = set()

    for M in possibleMs:
        for N in possibleNs:
            run = 0
            def test(i):
                return D[i] + A[i] == M or D[i] - B[i] == N
            for i in range(S):
                run = run + 1 if test(i) else 0
                if run > longest_run:
                    best_pair = (M, N)
                    longest_run = run

    for M in possibleMs:
        for N in possibleNs:
            run = 0
            start = 0
            def test(i):
                return D[i] + A[i] == M or D[i] - B[i] == N
            for i in range(S):
                run = run + 1 if test(i) else 0
                start = start if test(i) else i+1
                if run == longest_run:
                    maximal_sequences.add((start, i))

    print("Case #{}: {} {}".format(case, longest_run, len(maximal_sequences)))




