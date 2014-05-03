#!python3
import itertools

def squash(word):
    return "".join(x[0] for x in group(word))

def crib(word):
    return [x[1] for x in group(word)]

def group(word):
    last = None
    run = 0
    for letter in word:
        if letter == last:
            run += 1
        else:
            if run:
                yield (last, run)

            run = 1
            last = letter

    if run:
        yield (last, run)

assert squash("balla") == "bala"
assert crib("balla") == [1, 1, 2, 1]

def solve(words):
    """y is the minimum number of moves to make the strings identical. If there is no possible way to make all strings identical, print "Fegla Won" (quotes for clarity)."""
    squashed = [squash(word) for word in words]
    if len(set(squashed)) > 1:
        return "Fegla Won"

    cribs = [crib(word) for word in words]

    cost = 0

    for i in range(len(cribs[0])):
        # fix ith group
        disparate = [crib[i] for crib in cribs]

        possibles = []
        for x in disparate:
            possibles.append(sum(abs(y-x) for y in disparate))

        cost += min(possibles)

    return cost


if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    """The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing an integer N which is the number of strings. Followed by N lines, each line contains a non-empty string (each string will consist of lower case English characters only, from 'a' to 'z')."""

    T = int(f.readline())

    for case in range(1, T+1):
        N = int(f.readline())
        words = list()
        for i in range(N):
            words.append(f.readline())

        answer = solve(words)
        print("Case #{0}: {1}".format(case, answer))
