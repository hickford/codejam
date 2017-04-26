from collections import Counter

def solve_primary(s):
    counter = Counter(s)
    solution = ""

    last = None
    while counter:
        possibles = [pair[0] for pair in counter.most_common(3) if pair[0] != last]
        if not possibles:
            return False
            
        c = possibles[0]

        if len(possibles) > 1 and counter[possibles[0]] == counter[possibles[1]] and solution and possibles[1] == solution[0]:
           c = possibles[1]

        solution += c
        last = c
        counter.subtract([c])
        if counter[c] == 0:
            del counter[c]

    if len(solution) > 1 and solution[0] == solution[-1]:
        return False

    return solution

friends = set(["BR", "BY", "RY", "BO", "GR", "VY" ])

def adjacent(x, y):
    x, y = sorted([x, y])
    return x+y in friends

def solve(s):
    G = nx.Graph()
    for i, letter in enumerate(s):
        G.add_node(letter+str(i))

    for v in G.nodes():
        for w in G.nodes():
            if adjacent(v[0], w[0]):
                G.add_edge(v, w)

    cycle = nx.algorithms.tournament.hamiltonian_path(G)
    return "".join(p[0][0] for p in cycle)

import fileinput
f = fileinput.input()

T = int(f.readline())
for case in range(1, T+1):
    N, R, O, Y, G, B, V = [int(x) for x in f.readline().split()]
    s = "R" * R + "O" * O + "Y" * Y + "G" * G + "B" * B + "V" * V
    assert len(s) == N
    solution = solve(s) or "IMPOSSIBLE"
    print(f"Case #{case}: {solution}")

