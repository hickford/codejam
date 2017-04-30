# https://code.google.com/codejam/contest/dashboard?c=8294486#s=p2
"""It's the year 1860, and the Pony Express is the fastest mail delivery system joining the East and West coasts of the United States. This system serves N different cities. In each city, there is one horse (as in the expression "one-horse town"); each horse travels at a certain constant speed and has a maximum total distance it can travel before it becomes too tired to continue.

The Pony Express rider starts off on the starting city's horse. Every time the rider reaches a city, they may continue to use their current horse or switch to that city's horse; switching is instantaneous. Horses never get a chance to rest, so whenever part of a horse's maximum total distance is "used up", it is used up forever! When the rider reaches the destination city, the mail is delivered.

The routes between cities were established via complicated negotiations between company owners, lawmakers, union delegates, and cousin Pete. That means that the distances between cities do not necessarily follow common sense: for instance, they do not necessarily comply with the triangle inequality, and the distance from city A to city B might be different from the distance from city B to city A!

You are a time traveling entrepreneur, and you have brought a fast computer from the future. A single computer is not enough for you to set up an e-mail service and make the Pony Express obsolete, but you can use it to make optimal routing plans for the Pony Express. Given all data about routes between cities and the horses in each city, and a list of pairs of starting and ending cities, can you quickly calculate the minimum time necessary for each delivery? (You should treat all of these deliveries as independent; using cities/horses on one route does not make them unavailable on other routes.)"""

import numpy
from scipy.sparse.csgraph import floyd_warshall
import fileinput

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

f = fileinput.input()
T = int(f.readline())
for case in range(1, T+1):
    N, Q = (int(x) for x in f.readline().split())
    endurances, speeds = numpy.array([[int(x) for x in f.readline().split()] for i in range(N)]).T
    distances = numpy.array([[float(x) for x in f.readline().split()] for i in range(N)])
    distances[distances==-1] = numpy.inf
    
    distances = floyd_warshall(distances) 
    distances[distances > numpy.vstack(endurances)] = numpy.inf
    
    times = distances / numpy.vstack(speeds)
    times = floyd_warshall(times)

    starts, destinations = numpy.array([[int(x) for x in f.readline().split()] for i in range(Q)]).T
    solution = " ".join(str(times[u-1,v-1]) for u,v in zip(starts, destinations))
    print(f"Case #{case}: {solution}")
