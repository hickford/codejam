# https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard
"""A Whole New Word
Vincent and Desta are childhood friends. Today, Vincent is showing N distinct L-letter words to Desta by using some letter tiles. Each tile contains one uppercase English alphabet letter, and one number between 1 and L. A word consists of the letters spelled out by L tiles with numbers from 1 through L, in order. (Vincent's words are not necessarily real English words.)"""

from itertools import product

T = int(input())
for case in range(1, T+1):
    N, L = [int(x) for x in input().split()]
    words = [input() for i in range(N)]
    words.sort()
    letters = (sorted(set(w[i] for w in words)) for i in range(L)) # lazy generator
    all_words = ("".join(p) for p in product(*letters))
    solution = "-"
    for i, w in enumerate(all_words):
        if i >= len(words) or words[i] != w:
            solution = w
            break    

    print("Case #{}: {}".format(case, solution))
