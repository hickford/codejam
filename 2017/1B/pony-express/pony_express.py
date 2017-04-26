# https://code.google.com/codejam/contest/dashboard?c=8294486#s=p2
"""It's the year 1860, and the Pony Express is the fastest mail delivery system joining the East and West coasts of the United States. This system serves N different cities. In each city, there is one horse (as in the expression "one-horse town"); each horse travels at a certain constant speed and has a maximum total distance it can travel before it becomes too tired to continue.

The Pony Express rider starts off on the starting city's horse. Every time the rider reaches a city, they may continue to use their current horse or switch to that city's horse; switching is instantaneous. Horses never get a chance to rest, so whenever part of a horse's maximum total distance is "used up", it is used up forever! When the rider reaches the destination city, the mail is delivered.

The routes between cities were established via complicated negotiations between company owners, lawmakers, union delegates, and cousin Pete. That means that the distances between cities do not necessarily follow common sense: for instance, they do not necessarily comply with the triangle inequality, and the distance from city A to city B might be different from the distance from city B to city A!

You are a time traveling entrepreneur, and you have brought a fast computer from the future. A single computer is not enough for you to set up an e-mail service and make the Pony Express obsolete, but you can use it to make optimal routing plans for the Pony Express. Given all data about routes between cities and the horses in each city, and a list of pairs of starting and ending cities, can you quickly calculate the minimum time necessary for each delivery? (You should treat all of these deliveries as independent; using cities/horses on one route does not make them unavailable on other routes.)"""

from math import inf
import networkx as nx
from networkx.algorithms.shortest_paths import floyd_warshall, floyd_warshall_numpy

def solve_linear(N, Q, endurances, speeds, distances, starts, destinations):
    times = [inf for i in range(N)]
    times[0] = 0
    for i in range(N):
        # change horse at i
        time = times[i]
        speed = speeds[i]
        endurance = endurances[i]
        distance_on_horse = 0
        for j in range(i, N-1):
            distance_on_horse += distances[j][j+1]
            if distance_on_horse > endurance:
                break
            time += distances[j][j+1] / speed
            times[j+1] = min(times[j+1], time)

    return times[-1]

def solve(N, Q, endurances, speeds, distances, starts, destinations):
    assert len(endurances) == N
    assert len(speeds) == N
    assert len(distances) == N
    assert len(starts) == Q
    assert len(destinations) == Q

    G = nx.DiGraph()
    for i in range(N):
        G.add_node(i)
    for i in range(N):
        for j in range(N):
            if distances[i][j] == inf:
                continue
                
            assert 0 < distances[i][j] < inf    
            G.add_edge(i, j, weight=distances[i][j])

    M = floyd_warshall_numpy(G)

    G2 = nx.DiGraph()
    for i in range(N):
        G2.add_node(i)

    for i in range(N):
        distances_from_i = [M[i,j] for j in range(N)]
        distances_from_i = [d if d <= endurances[i] else inf for d in distances_from_i]
        times_from_i = [d / speeds[i] for d in distances_from_i]
        for j in range(N):
            if times_from_i[j] == inf:
                continue
            G2.add_edge(i, j, weight=times_from_i[j])

    N = floyd_warshall_numpy(G2)

    solutions = list()
    for start, destination in zip(starts, destinations):
        solutions.append(N[start,destination])

    return " ".join(str(x) for x in solutions)

import fileinput
f = fileinput.input()

T = int(f.readline())
for case in range(1, T+1):
    N, Q = [int(x) for x in f.readline().split()]
    endurances = list()
    speeds = list()
    for i in range(N):
        e, s = [int(x) for x in f.readline().split()]
        endurances.append(e)
        speeds.append(s)

    distances = list()
    for i in range(N):
        distances.append([int(x) if x != "-1" else inf for x in f.readline().split()])

    starts = list()
    destinations = list()
    for k in range(Q):
        u, v = [int(x) for x in f.readline().split()]
        assert 1 <= u <= N
        assert 1 <= v <= N
        starts.append(u-1)
        destinations.append(v-1)

    solution = solve(N, Q, endurances, speeds, distances, starts, destinations)
    print(f"Case #{case}: {solution}")
