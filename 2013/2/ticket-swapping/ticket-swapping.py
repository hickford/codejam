#!python3
# https://code.google.com/codejam/contest/2442487/dashboard#s=p0
"""The city has built its first subway line, with a grand total of N stations, and introduced a new way of paying for travel. Instead of just paying for one ticket and making an arbitrary journey, the price you pay is now based on entry cards..."""


def cost(d, N):
    """The cost of travelling distance d on a line with N stations"""
    assert 0 <= d <= N-1
    return d*N - d*(d-1)//2
	# worthy of note: when we come to compare swapping strategies, the d*N term in the cost function will cancel because the total distance travelled doesn't depend on how tickets are swapped. Still, I leave it in the cost function because positive costs are easier to think about.

def test_cost():
	"""unit test with examples from problem statement"""
	N = 10
	assert cost(0, N) == 0
	assert cost(1, N) == N
	assert cost(2, N) == 2*N-1
	assert cost(3, N) == 3*N-3
	assert cost(N-1, N) == (N**2 + N - 2)//2

test_cost()

def observe_shape():
	"""A long journey and a short journey is always cheaper than two medium journeys (with the same total distance). This is because cost per unit travel decreases for longer journeys."""
	N = 10
	assert cost(4, N) + cost(7, N) < cost(5, N) + cost(6, N)

observe_shape()

from collections import defaultdict, OrderedDict

def solve(journeys, N):
	naive_cost = 0
	for (start, end, frequency) in journeys:
		naive_cost += frequency * cost(end - start, N) 

	clever_cost = 0
	
	# for the clever cost, we aren't interested in individual passengers, only net change at each station
	change_by_station = defaultdict(int)
	for (start, end, frequency) in journeys:
		change_by_station[start] += frequency
		change_by_station[end] -= frequency

	change_by_station = OrderedDict(sorted(change_by_station.items()))
	assert sum(change_by_station.values()) == 0

	# model train on its journey, keeping track (no pun intended) of which stations tickets were bought at
	train = OrderedDict()	# tickets by station bought at
	for (station, change) in change_by_station.items():
		if change == 0:
			continue
		if change > 0:
			train[station] = change
		else:
			people_to_leave = -change
			while people_to_leave > 0:
				# by the observation, should first boot off people with tickets from most recent station (who are paying high unit cost) rather than those from earlier stations (paying cheap unit cost)
				last_station, last_lot = train.popitem()

				last_lot_to_leave = min(last_lot, people_to_leave)
				people_to_leave -= last_lot_to_leave
				clever_cost += last_lot_to_leave * cost(station - last_station, N)
				
				# if we popped too many people, put the remainder back as they were (at their original station, not this one)
				last_lot_to_remain = last_lot - last_lot_to_leave
				if last_lot_to_remain > 0:
					train[last_station] = last_lot_to_remain

	# end of the line, train is empty again
	assert len(train) == 0

	return naive_cost - clever_cost

if __name__ == "__main__":
	import fileinput
	f = fileinput.input()
	T = int(f.readline())
	for case in range(1,T+1):
		N, M = [int(x) for x in f.readline().split()]

		journeys = list()
		for i in range(M):
			start, end, frequency = [int(x) for x in f.readline().split()]
			journeys.append((start,end,frequency))

		answer = solve(journeys, N) % 1000002013
		print("Case #%d: %s" % (case, answer))